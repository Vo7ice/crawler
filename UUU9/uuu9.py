# coding=utf-8
__author__ = 'Vo7ice'
from bs4 import BeautifulSoup
import requests, re
import time
import sys


class Item:
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
        self.heroNames = []

    def getHeroList(self, url):
        """
        <a href="/hero/show/Oracle">
            <img hid="134"
                src="http://dota2dbpic.uuu9.com/2b1dc7ac-2c86-43f2-b743-61f53421bef814111513531135518.jpg"/>
            <span>神谕者</span>
        </a>
        """
        # req = requests.get(url, headers=self.headers)
        # print 'req status_code:%d' % req.status_code
        # if req.status_code == 200:
        soup = BeautifulSoup(open('index.html'), 'html.parser')
        content = soup.find_all(id='herolist1')
        pattern0 = re.compile('<span>.*?</span>')
        # target = re.findall(pattern0, content)
        # print 'target %s' % target
        # 数据为乱码 需要encode
        type = sys.getfilesystemencoding()
        # else:
        #    print 'network error!'

    def start(self):
        baseUrl = "http://db.dota2.uuu9.com/"
        self.getHeroList(baseUrl)


item = Item()
item.start()
