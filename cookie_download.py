import requests
import os
import json
import yaml
from retrying import retry
from fake_useragent import UserAgent

root_path = os.path.dirname(os.path.realpath(__file__))

def cookies_pool(cfg_file):
       with open(cfg_file, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
        return data["cookie"]


class CookieDownload:
    def __init__(self, cookie_file,proxy=None,**publish_cfg):
        self.cookie = None
        self.cookie_pool = cookies_pool(cfg_file=cookie_file)
        self.publish_methods = None
        self.tags = None
        self.proxy = proxy
        self.creat_publish_methods(**publish_cfg)
          
    def creat_publish_methods(self,**publish_methods):
        self.publish_methods = list(publish_methods.values())
        self.tags = list(publish_methods.keys())
        
    def download(self,doi,save_path):
        lable = 0
        for i, tag in enumerate(self.tags):
            method = self.publish_methods[i]
            if tag in doi:
                assert tag in list(self.cookie_pool.keys()) ,f'{tag} 无cookie记录!'
                idx = 0
                idx_len = len(self.cookie_pool[tag])
                assert idx_len > 0 ,f'{tag} 无cookie记录!'
                for _ in range(idx_len):
                    try:
                        self.cookie = self.cookie_pool[tag][idx]
                        # print(self.cookie)  ## 打印cookie
                        lable = method(doi,self.cookie,save_path,self.proxy)
                        if lable == 1:
                            break
                    except Exception as e:
                        print(e)
                        print(f'{tag}: {doi} 使用第{idx}个cookie下载失败,准备重试')
                        if idx < idx_len-1:
                            idx += 1
        return lable
    

# 预写好的下载方法，需要传入doi,cookie,output_dir,proxy

@retry(stop_max_attempt_number=3,wait_fixed=2)
def download_from_url(url,headers,save_path,proxy=None):
    """
    url: 完整的pdf下载地址
    
    hearders: 请求头
    
    save_path: 下载保存地址
    
    proxy: 代理地址（以及是否使用代理）
    """
    try:
        response = requests.get(url,headers=headers,stream=True,proxies={"http": "http://{}".format(proxy)})
        response.raise_for_status() 
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"下载成功：{save_path}")
        return 1
    except requests.RequestException as e:
        print(f"下载失败：{url}，原因：{str(e)}")
        return 0   


### 你的下载脚本的大概写法 需要有doi，cookie，output_dir,proxy几个形参，最终返回是否下载的lable，下载过程放在程序中完成   
                
def stroke(doi, cookies, save_path,proxy):  # stroke/AHA 期刊的下载 10.1161
    url = f"https://www.ahajournals.org/doi/pdf/{doi}"
    headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "max-age=0",
    "cookie": f"{cookies}",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": UserAgent().random,
    }
    lable = download_from_url(url,headers,save_path,proxy)
    return lable

def naturecom(doi,cookies,save_path,proxy):
    item = doi.replace('10.1038/','')
    url = f'https://www.nature.com/articles/{item}.pdf'
    headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "max-age=0",
    "cookie": f"{cookies}",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": UserAgent().random,
    }
    lable = download_from_url(url,headers,save_path,proxy)
    return lable
    
def springer_ER(doi,cookies,save_path,proxy):
    url = f"https://link.springer.com/content/pdf/{doi}.pdf"
    headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept_Encoding":"gzip,deflate",
    "cache-control": "max-age=0",
    "cookie": f"{cookies}",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": UserAgent().random,
    }
    lable = download_from_url(url,headers,save_path,proxy)
    return lable
        
        
if __name__ == '__main__':
    doi = "10.1007/s00330-024-10785-6"
    download_cfg ={'10.1161':stroke, '10.1038':naturecom,'10.1007':springer_ER  # 这里是使用特殊下载的定义处，其中stroke是stroke下载方法（见cookie_download.py）,"10.1161"是来自doi的发行商标识，   
}
    cook = CookieDownload(cookie_file=root_path+'/config.yaml',proxy=None)
    cook.creat_publish_methods(**download_cfg)
    lab = cook.download(doi,save_path=f"temp.pdf")
    print(lab)