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

        """
        <a href="/hero/show/Oracle">
            <img hid="134"
                src="http://dota2dbpic.uuu9.com/2b1dc7ac-2c86-43f2-b743-61f53421bef814111513531135518.jpg"/>
            <span>神谕者</span>
        </a>
        """

    def getHeroList(self, url):
        req = requests.get(url, headers=self.headers)
        print 'req status_code:%d' % req.status_code
        if req.status_code == 200:
            soup = BeautifulSoup(req.content, 'html.parser')
            i = 0
            type = sys.getfilesystemencoding()
            list = soup.find_all('div', 'picbox cl')
            print 'size:%d' % len(list)
            for link in soup.find_all('div', 'picbox cl'):
                print i
                hero = Hero()
                herolist = link.find_all('a')
                print 'list:%d' % len(herolist)
                hero_url = link.a['href']
                if link.a.contents[1].has_attr("hid"):
                    hero_id = link.a.contents[1]['hid']
                else:
                    good_id = link.a.contents[1]['gid']
                hero_img = link.a.contents[1]['src']
                hero_name = link.find('span')
                print 'url:%s, id:%s, img:%s, name:%s' % (hero_url, hero_id, hero_img, hero_name)

    def start(self):
        baseUrl = "http://db.dota2.uuu9.com/"
        self.getHeroList(baseUrl)


class Hero(object):
    @property
    def hero_url(self):
        return self.get('hero_url')

    @hero_url.setter
    def hero_url(self, value):
        return self.set('hero_url', value)

    @property
    def hero_id(self):
        return self.get('hero_id')

    @hero_id.setter
    def hero_id(self, value):
        return self.set('hero_id', value)

    @property
    def img_url(self):
        return self.get('img_url')

    @img_url.setter
    def img_url(self, value):
        return self.set('img_url', value)

    @property
    def name(self):
        return self.get('name')

    @name.setter
    def name(self, value):
        return self.set('name', value)

item = Item()
item.start()