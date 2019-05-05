import time
import io
import sys
import requests
import re
from lxml import etree
from bs4 import BeautifulSoup
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
class Kuanshou(object):

    def __init__(self):
        self.url = "https://live.kuaishou.com/cate/DQRM/?page="
        self.headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
            "Host":"live.kuaishou.com"
        }

    def get_req(self):
        for i in range(1,10):
            url = self.url + str(i)
            resp = requests.get(url=url, headers=self.headers)
            self.bs4_check(resp.text)
            # print(resp.text)
    
    def check_n(self, text):
        if isinstance(text, str):
            return text.replace("\n","").split()
        return str(text).replace("\n","").split()

    def bs4_check(self, html):
        soup = BeautifulSoup(html,"lxml")
        ul_list = soup.find_all(attrs={"class":"live-card-list"})  # 根据标签名获取
        for ul in ul_list:
            for li in ul.find_all(name="li"):
                try:
                    quality = self.check_n(li.find(class_="tag-quality").text)  # 品质
                    title = self.check_n(li.find(class_="live-card-following-info-title").text)  # 标题
                    class_ = self.check_n(li.find(class_="game-name").text)  # 分类
                    user = self.check_n(li.find(class_="user-info has-current-watching").text)  # 用户
                    count = self.check_n(li.find(class_="current-watching").text)
                    print(quality,title,class_,user,count)
                except Exception as e:
                    continue    
                


if __name__ == "__main__":
    kuaishou = Kuanshou()
    kuaishou.get_req()
