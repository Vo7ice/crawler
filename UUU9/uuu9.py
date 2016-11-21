# coding=utf-8
import logging
import leancloud
from requests.packages.urllib3.exceptions import ConnectionError
from Model import HeroSave, GoodSave, SkillSave
from leancloud import LeanCloudError

from bs4 import BeautifulSoup
import requests, re
import time
import sys

logging.basicConfig(level=logging.INFO)

__author__ = 'Vo7ice'


def checkHeroExsit(oid):
    HeroSave = leancloud.Object.extend('HeroSave')
    query = HeroSave.query
    try:
        hero_info = query.equal_to('oid', oid).find()[0]
    except IndexError as e:
        print 'error:', e.message
        hero_info = None
    return hero_info


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


class Item:
    global baseUrl

    def __init__(self):
        leancloud.init("tsVy6mtJMvQ1zhpnY4wdTVXo-gzGzoHsz", "gnJe9bgWGDfUaqaX5LQzyWHJ")
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
        baseUrl = "http://db.dota2.uuu9.com/"

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
                    heroInfo.set('href', hero['href']).save()
                    print 'hero_id%s' % hero.img['hid']
                    heroInfo.set('oid', hero.img['hid']).save()
                    print 'img_url%s' % hero.img['src']
                    heroInfo.set('img_src', hero.img['src']).save()
                    print 'name%s' % hero.span.string
                    heroInfo.set('name', hero.span.string).save()
                    i += 1
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
                    goodInfo.set('href', good['href']).save()
                    print 'good_id%s' % good.img['gid']
                    goodInfo.set('oid', good.img['gid']).save()
                    print 'img_url%s' % good.img['src']
                    goodInfo.set('img_src', good.img['src']).save()
                    print 'name%s' % good.span.string
                    goodInfo.set('name', good.span.string).save()
                    i += 1
            except leancloud.LeanCloudError as e:
                print e.message
        else:
            print 'network error'

    # 英雄列表
    def getHeroSimpleList(self, url):
        req = requests.get(url, headers=self.headers)
        print 'req status_code:%d' % req.status_code
        if req.status_code == 200:
            soup = BeautifulSoup(req.content, 'html.parser')
            tab = soup.find_all('tr', 'row row1')
            print 'list size:%d' % len(tab)
            for tr in tab:
                for index, td in enumerate(tr.findAll('td')):
                    print 'data:', td
                    if index == 0:  # 查询对象
                        hid = td.span.a['hid']
                        src = td.span.a.img['src']  # 获得src
                        href = td.span.a['href']  # 获得href
                        print 'gid:%s,src:%s,href:%s' % (hid, src, href)
                        hero_check = checkHeroExsit(hid)
                        if hero_check is None:
                            hero_info = HeroSave()
                            hero_info.set('oid', hid).save()
                            hero_info.set('img_src', src).save()
                            hero_info.set('href', href).save()
                        else:
                            hero_info = hero_check
                    elif index == 1:  # nickname
                        # print 'nickname:', td.findAll('a')[1].string
                        hero_info.set('name', td.findAll('a')[0].string).save()  # 存放name
                        hero_info.set('nickname', td.findAll('a')[1].string).save()  # 存放别称
                    elif index == 2:  # 技能
                        skills = td.findAll('a')
                        skill_list = []
                        for sk in skills:
                            print 'href%s,skill_id%s,img_url%s' % (sk['href'], sk.img['sid'], sk.img['src'])
                            skill_check = checkSkillExsit(sk.img['sid'])
                            if skill_check is None:
                                skill_info = SkillSave()
                                skill_info.set('href', sk['href']).save()
                                skill_info.set('oid', sk.img['sid']).save()
                                skill_info.set('img_src', sk.img['src']).save()
                                skill_info.set('hero_id', hid).save()
                            else:
                                skill_info = skill_check
                                skill_info.set('hero_id', hid).save()
                            skill_list.append(skill_info)
                        hero_info.set('skill', skill_list).save()
                    elif index == 3:  # 推荐装备
                        goods = td.findAll('a')
                        good_list = []
                        for good in goods:
                            gid = good.b['gid']
                            print 'gid:', gid
                            good_check = checkGoodExsit(gid)
                            if good_check is not None:
                                good_info = good_check
                            else:
                                good_info = GoodSave()
                                good_info.set('oid', good.b['gid']).save()
                                good_info.set('img_src', good.b.img['src']).save()
                                good_info.set('href', good['href']).save()
                                good_info.set('gold', good.span.string).save()
                            good_list.append(good_info)
                        hero_info.set('recommend', good_list).save()
        else:
            print 'network error'

    # 物品列表
    def getGoodSimpleList(self, good_url):
        req = requests.get(good_url, headers=self.headers)
        logging.info('req status_code:%d' % req.status_code)
        if req.status_code == 200:
            soup = BeautifulSoup(req.content, 'html.parser')
            tab = soup.find_all(name='tr', attrs={"class": re.compile("row row")})
            print 'tab size:%d' % len(tab)
            for tr in tab:
                for index, td in enumerate(tr.findAll('td')):
                    if index == 0:  # 查询对象
                        gid = td.span.a.img['gid']  # 获得gid
                        src = td.span.a.img['src']  # 获得src
                        href = td.span.a['href']  # 获得href
                        print 'gid:%s,src:%s' % (gid, src)
                        good_check = checkGoodExsit(gid)
                        if good_check is None:
                            good_info = GoodSave()
                            good_info.set('oid', gid).save()
                            good_info.set('img_src', src).save()
                            good_info.set('href', href).save()
                        else:
                            good_info = good_check
                    elif index == 1:
                        name = td.a.string  # name
                        print 'name%s' % name
                        good_info.set('name', name).save()
                    elif index == 2:  # 合成公式
                        goods = td.findAll('a')
                        composite_list = []
                        for good in goods:
                            print 'composite  id:%s,src:%s,href:%s' % (
                                good.img['gid'], good.img['src'], good['href'])
                            print 'gold:%s' % good.span.string
                            good_check = checkGoodExsit(good.img['gid'])
                            if good_check is None:  # 如果没有这个对象
                                composite = GoodSave()
                                composite.set('oid', good.img['gid']).save()
                                composite.set('img_src', good.img['src']).save()
                                composite.set('href', good['href']).save()
                            else:
                                composite = good_check
                            composite.set('gold', good.span.string).save()  # 设置金额
                            composite_list.append(composite)
                        good_info.set('composite', composite_list).save()
                    elif index == 3:  # 可合成物品
                        goods = td.findAll('a')
                        advanced_list = []
                        for good in goods:
                            print 'advanced id:%s,src:%s,href:%s' % (
                                good.img['gid'], good.img['src'], good['href'])
                            print 'gold%s' % good.span.string
                            good_check = checkGoodExsit(good.img['gid'])
                            if good_check is None:  # 如果没有这个对象
                                advanced = GoodSave()
                                advanced.set('oid', good.img['gid']).save()
                                advanced.set('img_src', good.img['src']).save()
                                advanced.set('href', good['href']).save()
                            else:
                                advanced = good_check
                            advanced.set('gold', good.span.string).save()
                            advanced_list.append(advanced)
                        good_info.set('advanced', advanced_list).save()
                    elif index == 4:  # 价格
                        good_info.set('gold', td.span.string).save()
        else:
            logging.error('network error')

    def start(self):
        # self.getHeroList(baseUrl)
        # self.getGoodList(baseUrl)
        # self.getHeroSimpleList(list_url)
        # self.getHeroSimpleList('http://db.dota2.uuu9.com/hero/list/?p=4')
        # self.getHeroSimpleList('http://db.dota2.uuu9.com/hero/list/?p=11')

        # 英雄列表
        for page in range(8, 12):
            if page == 1:
                hero_url = 'http://db.dota2.uuu9.com/hero/list/'
                self.getHeroSimpleList(hero_url)
                print 'page 1 ok'
            else:
                hero_url = 'http://db.dota2.uuu9.com/hero/list/?p='
                hero_url += str(page)
                self.getHeroSimpleList(hero_url)
                time.sleep(5)
                print 'page', page, ' okay!'

                # self.getGoodSimpleList('http://db.dota2.uuu9.com/goods/list/?p=3&')
                #
                # # 物品列表
                # for page in range(1, 16):
                #     if page == 1:
                #         good_url = 'http://db.dota2.uuu9.com/goods/list/'
                #         self.getGoodSimpleList(good_url)
                #         print 'page 1 okay!'
                #     else:
                #         good_url = 'http://db.dota2.uuu9.com/goods/list/?p='
                #         good_url += str(page)
                #         good_url += '&'
                #         self.getGoodSimpleList(good_url)
                #         time.sleep(5)
                #         print 'page ', page, ' okay!'


item = Item()
item.start()

"""
    <a href="/hero/show/Oracle">
        <img hid="134"
            src="http://dota2dbpic.uuu9.com/2b1dc7ac-2c86-43f2-b743-61f53421bef814111513531135518.jpg"/>
        <span>神谕者</span>
    </a>
"""

"""
<tr class="row row1">
    <td width="100">
        <span class="headpic"><a hid="134" href="/hero/show/Oracle">
            <img src="http://dota2dbpic.uuu9.com/2b1dc7ac-2c86-43f2-b743-61f53421bef814111513531135518.jpg" /><b></b></a></span>
    </td>
    <td width="120" class="heroname">
        <a href="/hero/show/Oracle"><b>神谕者</b></a><br />
        <a href="/hero/show/Oracle">奈里夫</a>
    </td>
    <td width="200" class="skillpic">
        <span class="picbox">
            <a href="/skill/show/Oracleq">
                <img sid="516" src="http://dota2dbpic.uuu9.com/bf61d5f4-5960-47e3-a028-05c3775c8b0a1.png" /><span class="key"></span></a>
            <a href="/skill/show/Oraclew">
                <img sid="517" src="http://dota2dbpic.uuu9.com/45b1d78f-a214-44a8-99b5-3b6fead389582.png" /><span class="key"></span></a>
            <a href="/skill/show/Oraclee">
                <img sid="518" src="http://dota2dbpic.uuu9.com/de3e0dcf-ca0a-4c36-b0fe-f67573cd3d4d3.png" /><span class="key"></span></a>
            <a href="/skill/show/Oracler">
                <img sid="519" src="http://dota2dbpic.uuu9.com/e90d9dd6-1adb-42fb-b397-f2957bf855ad4.png" /><span class="key"></span></a>
        </span>
    </td>
    <td width="279" class="equipic">
        <span class="picbox">
            <a href="/goods/show/BootsofTravel"><b gid="112">
                <img  src="http://dota2dbpic.uuu9.com/0091e871-edfd-4cfc-b261-ebc7ea9f7cfctravel_boots_lg.gif" /></b><span class="text">2450
            </span></a>
            <a href="/goods/show/Bloodstone"><b gid="144">
                <img  src="http://dota2dbpic.uuu9.com/017112bc-654a-4d5e-98fa-8a0a3223f59cxjs.png" /></b><span class="text">4950
            </span></a>
            <a href="/goods/show/GuinsoosScytheofVyse"><b gid="37">
                <img  src="http://dota2dbpic.uuu9.com/fdabc1a9-b8a5-486b-87c0-d1b82765bbaegs.jpg" /></b><span class="text">5675
            </span></a>
            <a href="/goods/show/RefresherOrb"><b gid="36">
                <img  src="http://dota2dbpic.uuu9.com/7d17beec-b25a-47e0-9350-8f29f7185cearb.jpg" /></b><span class="text">5300
            </span></a>
            <a href="/goods/show/RodofAtos"><b gid="33">
                <img  src="http://dota2dbpic.uuu9.com/b35d8b21-d19f-41fb-bf26-c7c70d22bf06ra.jpg" /></b><span class="text">3100
            </span></a>
            <a href="/goods/show/ShivasGuard"><b gid="130">
                <img  src="http://dota2dbpic.uuu9.com/9b48b02b-b58c-4595-8a5f-b8a4d494d753swdsh.gif" /></b><span class="text">4700
            </span></a>
        </span>
    </td>
</tr>
"""
"""
<tr class="row row2">
    <td width="80" class="equipic">
        <span class="picbox"><a href="/goods/show/ mango">
            <img gid="201" src="http://dota2dbpic.uuu9.com/56acc93c-c871-428c-af78-527b2c910d071.png" /></a> </span>
    </td>
    <td width="120" class="heroname">
        <a href="/goods/show/ mango">魔法芒果</a>
    </td>
    <td width="195" class="equipic">
        <span class="picbox">
        </span>
    </td>
    <td width="195" class="equipic">
        <span class="picbox">
        </span>
    </td>
    <td width="109">
        <span class="gold">150</span>
    </td>
</tr>
"""
