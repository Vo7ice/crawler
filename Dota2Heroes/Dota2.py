# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests,re
import time
import sys

class Dota2:
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
        
    def getContent(self,url):
        req = requests.get(url,headers=self.headers)
        print 'req status_code:%d' % req.status_code
        if (req.status_code == 200):
            # print 'source:%s' % req.content
            pattern0 = re.compile('<option value=.*?</option>')
            target = re.findall(pattern0,req.content)
            # 数据为乱码 需要encode
            type = sys.getfilesystemencoding()
            with open('Heros.json','a') as file:
                file.write('{"Heros":[')
                for x in target:
                    # print 'x:%s' % x.decode('UTF-8').encode(type)[14:-9]
                    temp = x.decode('UTF-8').encode(type)[14:-9]
                    temp0,temp1 = temp.split('>')
                    file.write('{')
                    file.write(temp0)
                    file.write(':"')
                    file.write(temp1)
                    file.write('"},')    
                file.write(']}')
                file.close()
        else:
            print '网络状态异常'
            
    def start(self):
        baseUrl = "http://www.dota2.com.cn/heroes/"
        self.getContent(baseUrl)

dota2 = Dota2()
dota2.start()
