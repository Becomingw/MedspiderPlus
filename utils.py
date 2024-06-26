import pandas as pd
import requests
import json
import os
import openai
import re
import openpyxl
from zhipuai import ZhipuAI
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from retrying import retry
import yaml
from cookie_download import *

download_cfg ={'10.1161':stroke,'10.1038':naturecom,'10.1007':springer_ER         # 这里是使用特殊下载的定义处，其中stroke是stroke下载方法（见cookie_download.py）,"10.1161"是来自doi的发行商标识，   
}

root_path = os.path.dirname(os.path.realpath(__file__))


def read_yaml(yaml_path):
    with open(yaml_path, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
    return data

def get_proxy(shift=False):  # 加入代理访问
    if shift:
        url =  "https://proxypool.scrape.center/random"
        return requests.get(url).text.strip()
    else:
        proxy_dic = requests.get("http://demo.spiderpy.cn/get/").json()
        return proxy_dic.get("proxy")

@retry(stop_max_attempt_number=3, wait_fixed=2)
def great_url_responce(kw,page,year,proxy):
    params_dic ={
        'term': kw,
        'page': str(page),
        'filter': f'datesearch.y_{year}',
        'format': 'abstract',
    }
    if proxy:
        reponse = requests.get('https://pubmed.ncbi.nlm.nih.gov/',
                            params=params_dic,
                            headers={"User-Agent": UserAgent().random},
                            proxies={"http": "http://{}".format(proxy)})
    else:
        reponse = requests.get('https://pubmed.ncbi.nlm.nih.gov/',
                            params=params_dic,
                            headers={"User-Agent": UserAgent().random}
                            )
    return reponse


## 使用OpenAI系来进行生成

def contains_chinese(s):
    for char in s:
        if '\u4e00' <= char <= '\u9fff':
            s.replace(char,"")
    return True

@retry(stop_max_attempt_number=4, wait_fixed=2)
def openai_research(kw,openkey,md="gpt-3.5-turbo",proxy='https://api.surger.xyz/v1'):
    if not proxy:
        pass
    else:
        openai.api_base = proxy
    if "moonshot" in md:
        openai.api_base = "https://api.moonshot.cn/v1"
    openai.api_key = openkey
    completion = openai.ChatCompletion.create(
        model=md,
        temperature = 0.7,
        messages=[
            {"role": "user", "content": "你是一位精通PubMed检索的学者，请你分析我的研究内容。基于PubMed语法构建检索公式，直接提供最终的PubMed检索公式（不用对回答进行解释）,且检索式不能包含中文。我的研究是："+kw}
        ]
    )
    key_word = completion.choices[0].message['content']
    _ = contains_chinese(key_word)
    return key_word  


@retry(stop_max_attempt_number=4, wait_fixed=2)
def GLM_reaserch(kw,key):
        client = ZhipuAI(api_key=key)
        response = client.chat.completions.create(
            model="glm-4",  # 填写需要调用的模型名称
            temperature = 0.7,
            messages=[
                {
                    "role": "user",
                    "content": "你是一位精通PubMed检索的学者，请你分析我的研究内容。基于PubMed语法构建检索公式，直接提供最终的PubMed检索公式（不用对回答进行解释）,且检索式不能包含中文。我的研究是："+kw
                }
            ]
        )
        kword = response.choices[0].message.content
        return kword


## Gemin proxy 2 GPT
def Gemini(data,apikey):
    url = 'https://proxy.surger.xyz/v1/chat/completions'
    headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {apikey}',
    }
    data = data
    response = requests.post(url, headers=headers, data=json.dumps(data))
    res_text = response.text
    res_js = json.loads(res_text)
    return res_js["choices"][0]["message"]["content"]

@retry(stop_max_attempt_number=4, wait_fixed=2)
def Gemini_research(kw,openkey,proxy='https://api.surger.xyz/v1'):
    if not proxy:
        data = {
        'model': 'gpt-3.5-turbo',
        'messages': [{'role': 'user', 'content': "你是一位精通PubMed检索的学者，请你分析我的研究内容。基于PubMed语法构建检索公式，直接提供最终的PubMed检索公式（不用对回答进行解释）,且检索式不能包含中文。我的研究是："+kw}],
        'temperature': 0.7,
        }
        response = Gemini(data,openkey)
    else:
        openai.api_base = proxy
        openai.api_key = openkey
        completion = openai.ChatCompletion.create(
        model="gemini-pro",
        temperature = 0.7,
        messages=[
            {"role": "user", "content": "你是一位精通PubMed检索的学者，请你分析我的研究内容。基于PubMed语法构建检索公式，直接提供最终的PubMed检索公式（不用对回答进行解释）,且检索式不能包含中文。我的研究是："+kw}
        ]
        )
        response = completion.choices[0].message['content']
    return response



# 查找文献主程序部分
def main(pages, kw, year,excel_path,progress_callback,proxy=None):
    paper_data = pd.DataFrame(columns=['title', 'journal', 'Date', 'doi', "abstract", 'PMID', 'journal_link',
                                       'free_link', 'download'])
    if pages < 0:
        pages = 1
    pages += 1
    for page in range(1, pages):
        progress_callback(int((page / (pages-1)) * 100))
        response = great_url_responce(kw,page,year,proxy)
        response.raise_for_status()  # 防止没正确解析出现错误运行
        response.encoding = response.apparent_encoding  # 防止乱码

        soup = BeautifulSoup(response.text, 'html.parser')

        paper_list = soup.find_all('div', attrs={"class": "results-article"})


        paper_record = {}
        for paper in paper_list:
            title = []
            # 清空字典
            paper_record.clear()
            article = paper.article
            titles = article.h1.a.strings
            # strip函数用于删除头尾的空白符,包括\n\t等
            for s in titles:
                title.append(s.strip())
            paper_record['title'] = ''.join(title)
            # 获取发表年份
            date_tem = article.find('span', attrs={'class': 'cit'})
            try:
                date = date_tem.text[0:4]
                paper_record['Date'] = date + '年'
            except:
                pass
            # 获取DOI信息
            doi = article.find('span', attrs={"class": "citation-doi"})
            if doi is None:
                paper_record['doi'] = 'No doi'
            else:
                paper_record['doi'] = doi.string.strip()[5:-1]

            # 获取PMID
            try:
                PMID = article.find('strong', attrs={"class": "current-id"})
                pmid = ''.join(filter(str.isdigit, PMID.text))
                paper_record['PMID'] = pmid
            except:
                pass
            # 获取文章地址
            try:
                PMIC_tem = article.find('a', attrs={"class": "id-link"})
                PMIC_link = PMIC_tem.get('href')
                if PMIC_link.startswith('http://www.ncbi.nlm.nih.gov'):
                    paper_record['free_link'] = PMIC_link
                else:
                    paper_record['journal_link'] = PMIC_link
            except:
                pass
            # 获取期刊
            journal_temp = article.find('button', attrs={'class': 'journal-actions-trigger trigger'})
            try:
                journal = journal_temp.get('title')
                paper_record['journal'] = journal
            except:
                pass
            # 获取摘要信息
            abstract = []
            abstracte = []
            if article.find_all("em", attrs={"class": "empty-abstract"}):
                abstract.append("No abstract")
            else:
                content = article.find("div", attrs={"class": "abstract-content selected"})
                abstracts = content.find_all('p')

                for item in abstracts:
                    for sub_content in item.strings:
                        abstracte.append(sub_content.strip())
                paper_record['abstract'] = ''.join(abstracte)
            paper_tem = pd.DataFrame(paper_record, index=[0])
            paper_data = pd.concat([paper_data, paper_tem], ignore_index=True)
    try:
        paper_data.to_excel(excel_path, index=False)
        return f"查找结束！共计【{len(paper_data['title'])}】篇文献,存储地址：{excel_path}"
    except:
        return '不关Excel，保存失败，重新再来一次吧！'
    



# 文献下载部分
def Pubmed_download(excel,pdf_folder,progress_callback,proxy=None):
    print('开始下载.....')
    df = pd.read_excel(excel, engine='openpyxl')
    ok_paper = len(df[df['download'] == 1])
    for index, link in df.iterrows():
        if type(link['free_link']) == type('str') and link['download'] != 1:
            Tl = re.sub(r'[\\/:*?"<>|]', '_', link['title'])
            p_url = link['free_link']
            if proxy:
                response = requests.get(url=p_url, headers={"User-Agent": UserAgent().random},proxies={"http": "http://{}".format(proxy)})
            else:
                response = requests.get(url=p_url, headers={"User-Agent": UserAgent().random})
            response.raise_for_status()
            response.encoding = response.apparent_encoding
            soup = BeautifulSoup(response.text, 'html.parser')
            if type(soup) == None:
                continue
            link_tem = soup.find('li', attrs={'class': 'pdf-link other_item'})
            real_link = link_tem.find('a').get('href')
            real_link = 'https://www.ncbi.nlm.nih.gov' + real_link
            if proxy:
                response = requests.get(url=real_link, headers={"User-Agent": UserAgent().random},proxies={"http": "http://{}".format(proxy)})
            else:
                response = requests.get(url=real_link, headers={"User-Agent": UserAgent().random})
            if response.status_code == 200:
                if os.path.exists(pdf_folder):
                    pass
                else:
                    os.makedirs(pdf_folder)
                with open(f'{pdf_folder}/{Tl}.pdf', 'wb') as file:
                    file.write(response.content)
                print(f"[{Tl}] has been downloaded!")
                df.at[index, 'download'] = 1
                ok_paper+=1
                progress_callback(int((ok_paper / len(df['title'])) * 100))
            else:
                print(f"[{Tl}] failed to be downloaded!")
                df.at[index, 'download'] = 0
        else:
            df.at[index, 'download'] = 0
    try:
        df.to_excel(excel, engine='openpyxl', index=False)
    except:
        print('请关闭excel文件后重试，本次表格写入失败！')
    print('PubMed Downloaded over!')



def sci_hub(doi, folder, filename, proxy=None):
    output_folder = folder
    scihubs = ["https://www.sci-hub.st/","https://www.sci-hub.se/"]
    for idx in range(2):
        try:
            scihub_url = scihubs[idx]
            if proxy:
                response = requests.post(scihub_url, data={"request": doi},proxies={"http": "http://{}".format(proxy)})
            else:
                response = requests.post(scihub_url, data={"request": doi})
            break
        except:
            if idx >= 1:
                return 0
            else:
                continue
    soup = BeautifulSoup(response.content, features="html.parser")
    flag = False
    n = 0
    try:
        buttons_div = soup.find('div', {'id': 'buttons'})
        download_button = buttons_div.find('button')
        download_url = download_button['onclick'][15:-1]
        flag = True
        n = 1
    except:
        print(f'[{doi}] has no target')
    while flag:
        if download_url.startswith('//'):
            print(download_url[2:-14])
            pdf_response = requests.get("https://" + download_url[2:-14], stream=True,proxies=proxy)
        else:
            pdf_url = scihub_url + download_url
            pdf_url = pdf_url[0:-14]
            pdf_response = requests.get(pdf_url, stream=True)
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        if filename:
            filename = filename
        else:
            filename = doi.replace('/', '_')
        local_filename = os.path.join(output_folder, f"{filename}.pdf")
        with open(local_filename, 'wb') as f:
            for chunk in pdf_response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        print(f'[{filename}] has been downloaded!')
        flag = False
    return n

# 使用cookie来下载
def read_cookies(cookies_path,publish_name):
    with open(cookies_path, 'r') as f:
        data = f.read()
        cookies = json.loads(data)
        cookie = cookies[publish_name][0]
    return cookie 

def download_operation(excel_path,pdf_folder,progress_callback,proxy=None):
        Pubmed_download(excel_path,pdf_folder,progress_callback,proxy)
        spicial_dwonloader = CookieDownload(cookie_file=root_path+"\\config.yaml",proxy=proxy,**download_cfg)  # cookie下载器实例
        Df = pd.read_excel(excel_path, engine='openpyxl')
        all_paper = len(Df['download'])
        ok_paper = len(Df[Df['download'] == 1])
        progress_callback(int((ok_paper / all_paper) * 100))
        for index, raw in Df.iterrows():
            if raw['download'] == 0:
                flag = sci_hub(raw['doi'],pdf_folder, filename=re.sub(r'[\\/:*?"<>|]', '_', raw['title']),proxy=proxy)
                if flag==0 : 
                    flag = spicial_dwonloader.download(doi=raw['doi'], save_path=pdf_folder+"/"+re.sub(r'[\\/:*?"<>|]', '_', raw['title'])+".pdf")
                Df.at[index, 'download'] = flag
                ok_paper+=1
                progress_callback(int((ok_paper / all_paper) * 100))
        try:
            Df.to_excel(excel_path, engine='openpyxl', index=False)
        except:
            print('请关闭excel文件后重试，本次表格写入失败！')
        progress_callback(int((all_paper/ all_paper) * 100))
        print('Download all over!')


if __name__ =="__main__":
    

    coo = read_cookies(root_path+"/cookie.txt",'AHA')
    print(coo)


    # main(1,"cancer")
    # url = 'https://pubmed.ncbi.nlm.nih.gov/'
    # response = great_url_responce(url,"canceer",1)
    # print(response)
