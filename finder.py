import random
import os
from utils import *

father_path = os.getcwd()

class Gpt_finder:
    def __init__(self):
        self.use_ai = True
        self.model = 0
        self.pages = 10
        self.year = 5
        self.proxy = None
        self.gpt_proxy = "https://api.surger.xyz/v1"
        self.apikey = None
        self.excel_save_path = father_path+"/MedSpider_save.xlsx"
        self.custom_model = None

    def set_model(self,model):
        self.model = model
        
    def set_pages(self,pages):
        self.pages = pages
        print("已设置保存数:",pages)
        
    def set_year(self,year):
        self.year = year
        print("已设置纳入年数:",year)
        
    def set_proxy(self,proxy):
        self.proxy = proxy

    def find_reserch(self,query,key,progress_callback):
        if self.use_ai:
           return self.find_reserch_ai(query,key,progress_callback)
        else:
            return self.find_reserch_manual(query,progress_callback)
        
    def choose_model(self,query):
        if self.model == 0:
            print("模型已设置为：gpt3.5turbo")
            return openai_research(query,self.apikey,"gpt-3.5-turbo",proxy=self.gpt_proxy)
        elif self.model == 1:
            print("模型已设置为：Kimi")
            return openai_research(query,self.apikey,"moonshot-v1-8k",proxy=self.gpt_proxy)
        elif self.model == 2:
            print("模型已设置为：gpt4")
            return openai_research(query,self.apikey,"gpt-4",proxy=self.gpt_proxy)
        elif self.model == 4:
            print("模型已设置为：glm4")
            return GLM_reaserch(query,self.apikey)
        elif self.model == 3:
            print("模型已设置为：gemini")
            return Gemini_research(query,self.apikey,self.gpt_proxy)
        elif self.model == 5:
            print(f"模型已设置为：{self.custom_model}")
            return openai_research(query,self.apikey,self.custom_model,proxy=self.gpt_proxy)
        else:
            raise Exception("model will coming soon")
        
    def find_reserch_manual(self,query,progress_callback):
        true_pages = int(self.pages/10)
        result = main(true_pages,query,self.year,self.excel_save_path,progress_callback,self.proxy)
        return result

    def find_reserch_ai(self,query,key,progress_callback):
        self.apikey = key
        if self.apikey is None:
            raise Exception("API key is required for AI search")
        kw = self.choose_model(query)
        print("生成关键词:",kw)
        true_pages = int(self.pages/10)
        result = main(true_pages,kw,self.year,self.excel_save_path,progress_callback,self.proxy)
        return kw+"\n"+result

    def download_pdf(self,progress_callback):
        return download_operation(self.excel_save_path,progress_callback=progress_callback,proxy=self.proxy)


if __name__ =="__main__":
    print(os.path.dirname(os.getcwd()))
        

