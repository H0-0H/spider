import re
import sys
import time
import io
import random
import datetime
import requests
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

class Maoyan(object):
    def __init__(self,headers, url):
        self.headers = headers
        self.url = url

    def get_req(self):
        for i in range(0,100,10):
            url = self.url + str(i)
            resp = requests.get(url=self.url,headers=self.headers)
            time_sleep = random.uniform(1,5)
            time.sleep(time_sleep)
            self.re_check(resp.text)

    def re_check(self,html):
        pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
        img_href_results = re.findall(pattern,html)
        self.inster_sql(img_href_results)
    
    def inster_sql(self,inster_like):
        k = []
        for i in inster_like:
            # print(i)
            ph = i[0]
            img = i[1]
            title = i[2]
            zy = i[3].replace("\r",'').replace("\n","").replace("\t","").strip()
            time_on = i[4]
            pf = i[5]+i[6]
            k.append([ph,img,title,zy,time_on,pf])
        print(k)

if __name__ == "__main__":
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    "Host": "maoyan.com",
    }   
    url = "https://maoyan.com/board/4?offset="
    maoyan = Maoyan(headers,url)
    maoyan.get_req()
