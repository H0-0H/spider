import sys
import io
import requests
from pyquery import PyQuery as pq
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
class Huajiao():
    def __init__(self):
        self.heades = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
        }

    def get_huashu(self):
        resp = pq(url="http://www.huajiao.com/category/1000")
        self.check_resp(resp)

    def check_str(self, str_l):
        s = str(str_l).replace("\n","").replace("\r","")
        return s


    
    def get_room(self,url):
        url_to = "http://www.huajiao.com" + url
        resp = pq(requests.get(url=url_to,headers=self.heades).text)
        pm = resp(".js-player-uid .content").text()
        tag = resp(".author-info-box .js-tags").text()
        index = resp(".author-info-box .statics-base").text()
        return pm,tag,self.check_str(index)

    def check_resp(self,html):
        ul = html(".js-list-ul")
        li = ul.children().items()
        for test in li:
            a = test.children("a")
            if not a:
                continue
            href = a.attr("href")
            id,tag,index = self.get_room(href)
            img = a(".img").attr("src")
            title = a(".fl").text()
            count = a(".fr").text()
            print(id,img,title,count,tag,index)

if __name__ == "__main__":
    huajiao = Huajiao()
    huajiao.get_huashu()