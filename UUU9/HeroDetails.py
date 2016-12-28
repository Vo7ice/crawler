# coding=utf-8
from bs4 import BeautifulSoup
import leancloud
import requests
from Config import base_url

__author__ = 'Vo7ice'


def checkGoodExsit(oid):
    GoodSave = leancloud.Object.extend('GoodSave')
    query = GoodSave.query
    try:
        good_info = query.equal_to('oid', oid).find()[0]
    except IndexError as e:
        print 'error:', e.message
        good_info = None
    return good_info


def checkSkillExsit(oid):
    SkillSave = leancloud.Object.extend('SkillSave')
    query = SkillSave.query
    try:
        skill_info = query.equal_to('oid', oid).find()[0]
    except IndexError as e:
        print 'error:', e.message
        skill_info = None
    return skill_info


class HeroDetails(object):
    """
    收集Hero的详情

    """

    def __init__(self, hero):
        self.hero = hero
        self.hero_id = hero.get('oid')
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}

    def start(self):
        self.get_detail(base_url + self.hero.get('href'))

    def get_detail(self, url):
        print 'start get hero %s detail.' % self.hero.get('name')
        req = requests.get(url, headers=self.headers)
        print 'req status_code:%d' % req.status_code
        if req.status_code == 200:
            soup = BeautifulSoup(req.content, 'html.parser')
            background = soup.find('div', {'class': 'herotext r'})
            self.hero.set('background', background.p.string)  # 设置英雄的背景故事
            contents = soup.find('div', {'class': 'content jianbg'})
            self.set_property(contents)  # 设置英雄的基础属性
            self.set_attribute_index(soup)  # 设置英雄的指数
            self.set_goods_points(soup)  # 设置英雄的装备和技能加点
        else:
            print 'network error'

    def set_goods_points(self, soup):
        info_list = soup.find('div', {'class': 'picbox cl'})
        print 'info_list:', len(info_list)
        begin = []
        early = []
        core = []
        available = []
        points = []
        for index, item in enumerate(info_list):
            if index == 1:
                self.get_goodlist(begin, item)
            if index == 2:
                self.get_goodlist(early, item)
            if index == 3:
                self.get_goodlist(core, item)
            if index == 4:
                self.get_goodlist(available, item)
            if index == 5:
                self.get_pointlist(points, item)
        self.hero.set('begin', begin).save()
        self.hero.set('early', early).save()
        self.hero.set('core', core).save()
        self.hero.set('available', available).save()
        self.hero.set('points', points).save()

    @staticmethod
    def get_goodlist(attribute, item):
        tmp = item.find_all('a')
        for x in tmp:
            good = checkGoodExsit(x.img['gid'])
            attribute.append(good)

    @staticmethod
    def get_pointlist(attribute, item):
        tmp = item.find_all('a')
        for x in tmp:
            skill = checkSkillExsit(x.img['gid'])
            attribute.append(skill)

    # 属性指数
    def set_attribute_index(self, soup):
        index_html = soup.find('b', {'class': 'l'})
        print 'attribute index`s size:', len(index_html)
        attribute_index = []
        for i in index_html:
            attribute_index.append(i.string)
        self.hero.set('attribute_index', attribute_index).save()

    # 基础属性
    def set_property(self, contents):
        properties = contents[0]
        print 'property size:', len(properties.find_all('span'))
        base_property = []
        for pr in properties.find_all('span'):
            base_property.append(pr.string)
        self.hero.set('base_property', base_property).save()
