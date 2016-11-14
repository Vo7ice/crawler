# coding=utf-8
import leancloud

__author__ = 'Vo7ice'
from bs4 import BeautifulSoup
import requests, re
import time
import sys
from leancloud import Object


class Item:
    def __init__(self):
        leancloud.init("tsVy6mtJMvQ1zhpnY4wdTVXo-gzGzoHsz", "gnJe9bgWGDfUaqaX5LQzyWHJ")
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}

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
            # i = 0
            # type = sys.getfilesystemencoding()
            # all = soup.find_all('div', 'picbox cl')
            # print 'size:%d' % len(all)
            herolist = soup.find('div', id='herolist1')
            heroes = herolist.findAll('a')
            i = 0
            try:
                for hero in heroes:
                    print i
                    heroInfo = HeroSave()
                    print 'href%s' % hero['href']
                    heroInfo.set('hero_url', hero['href']).save()
                    print 'hero_id%s' % hero.img['hid']
                    heroInfo.set('hero_id', hero.img['hid']).save()
                    print 'img_url%s' % hero.img['src']
                    heroInfo.set('img_url', hero.img['src']).save()
                    print 'name%s' % hero.span.string
                    heroInfo.set('name',hero.span.string).save()
                    i = i + 1
            except leancloud.LeanCloudError as e:
                print e.message
        else:
            print 'network error'

    def getGoodList(self, url):
        req = requests.get(url, headers=self.headers)
        print 'req status_code:%d' % req.status_code
        if req.status_code == 200:
            soup = BeautifulSoup(req.content, 'html.parser')
            goodlist = soup.find('div', id='goodslist1')
            goods = goodlist.findAll('a')
            i = 0
            try:
                for good in goods:
                    print i
                    goodInfo = GoodSave()
                    print 'href%s' % good['href']
                    goodInfo.set('good_url', good['href']).save()
                    print 'good_id%s' % good.img['gid']
                    goodInfo.set('good_id', good.img['gid']).save()
                    print 'img_url%s' % good.img['src']
                    goodInfo.set('img_url', good.img['src']).save()
                    print 'name%s' % good.span.string
                    goodInfo.set('name',good.span.string).save()
            except leancloud.LeanCloudError as e:
                print e.message
        else:
            print 'network error'

    def start(self):
        baseUrl = "http://db.dota2.uuu9.com/"
        # self.getHeroList(baseUrl)
        self.getGoodList(baseUrl)


class HeroSave(Object):
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
    def hero_name(self):
        return self.get('hero_name')

    @hero_name.setter
    def hero_name(self, value):
        return self.set('hero_name', value)


class GoodSave(Object):
    @property
    def good_url(self):
        return self.get('good_url')

    @good_url.setter
    def good_url(self, value):
        return self.set('good_url', value)

    @property
    def good_id(self):
        return self.get('good_id')

    @good_id.setter
    def good_id(self, value):
        return self.set('good_id', value)

    @property
    def img_url(self):
        return self.get('img_url')

    @good_url.setter
    def img_url(self, value):
        return self.set('img_url', value)

    @property
    def good_name(self):
        return self.get('good_name')

    @good_name.setter
    def good_name(self, value):
        return self.set('good_name', value)


item = Item()
item.start()
