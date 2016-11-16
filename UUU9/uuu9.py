# coding=utf-8
import leancloud
from Model import HeroSave, GoodSave, SkillSave

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

    def getHeroSimpleList(self, url):
        req = requests.get(url, headers=self.headers)
        print 'req status_code:%d' % req.status_code
        if req.status_code == 200:
            soup = BeautifulSoup(req.content, 'html.parser')
            tab = soup.find_all('tr', 'row row1')
            print 'list size:%d' % len(tab)
            # datas = datalist.find('tr')
            # print 'list size:%d' % len(datas)
            for tr in tab:
                for index, td in enumerate(tr.findAll('td')):
                    if index == 0:  # 查询对象
                        hid = td.span.a['hid']
                        HeroSave = leancloud.Object.extend('HeroSave')
                        query = HeroSave.query
                        hero_info = query.equal_to('oid', hid).find()[0]
                    elif index == 1:  # nickname
                        # print 'nickname:', td.findAll('a')[1].string
                        hero_info.set('nickname', td.findAll('a')[1].string).save()
                    elif index == 2:  # 技能
                        skills = td.findAll('a')
                        skill_list = []
                        for sk in skills:
                            skillInfo = SkillSave()
                            print 'href%s' % sk['href']
                            skillInfo.set('skill_url', sk['href']).save()
                            print 'skill_id%s' % sk.img['sid']
                            skillInfo.set('skill_id', sk.img['sid']).save()
                            print 'img_url%s' % sk.img['src']
                            skillInfo.set('img_url', sk.img['src']).save()
                            skill_list.append(skillInfo)
                        hero_info.set('skill', skill_list).save()
                    elif index == 3:  # 推荐装备
                        goods = td.findAll('a')
                        good_list = []
                        for good in goods:
                            query = GoodSave.query
                            gid = good.b['gid']
                            print 'gid:', gid
                            try:
                                good_info = query.equal_to('oid', gid).find()[0]
                            except IndexError as e:
                                good_info = None
                            good_list.append(good_info)
                        hero_info.set('recommend', good_list).save()
        else:
            print 'network error'

    def start(self):
        baseUrl = "http://db.dota2.uuu9.com/"
        # self.getHeroList(baseUrl)
        # self.getGoodList(baseUrl)
        list = '/hero/list/'
        list_url = baseUrl + list
        # self.getHeroSimpleList(list_url)
        self.getHeroSimpleList('http://db.dota2.uuu9.com/hero/list/?p=4')
        self.getHeroSimpleList('http://db.dota2.uuu9.com/hero/list/?p=12')

        # for page in range(10, 12):
        #     if page == 0:
        #         list_url = 'http://db.dota2.uuu9.com/hero/list/'
        #         self.getHeroSimpleList(list_url)
        #         print 'page 1 ok'
        #     else:
        #         list_url = 'http://db.dota2.uuu9.com/hero/list/?p='
        #         list_url += str(page)
        #         self.getHeroSimpleList(list_url)
        #         time.sleep(5)
        #         print 'page', page, ' ok'


item = Item()
item.start()

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
