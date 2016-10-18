# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests, re
import time
import sys


class Dota2:
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
        self.heros = []

    def getHeroNames(self, url):
        req = requests.get(url, headers=self.headers)
        print 'req status_code:%d' % req.status_code
        if req.status_code == 200:
            # print 'source:%s' % req.content
            pattern0 = re.compile('<option value=\"[a-z_]{4,}\">.*?</option>')
            target = re.findall(pattern0, req.content)
            target = target[2:]
            # print 'target:%s' % target
            # 数据为乱码 需要encode
            type = sys.getfilesystemencoding()
            with open('Heroes.json', 'a') as file:
                file.write('{"Heroes":[')
                for x in target:
                    # print 'x:%s' % x.decode('UTF-8').encode(type)[14:-9]
                    temp = x.decode('UTF-8').encode(type)[14:-9]
                    temp0, temp1 = temp.split('>')
                    file.write('{"name":')
                    file.write(temp0)
                    self.heros.append(temp0[1:-1])
                    file.write(',"cname":"')
                    file.write(temp1)
                    file.write('","hoverLarge":"/images/heroes/')
                    file.write(temp0[1:-1])
                    file.write('_hphover.png"')
                    file.write(',"hoverSmall":"/images/heroes/')
                    file.write(temp0[1:-1])
                    file.write('_sb.png"')
                    file.write('},')
                file.write(']}')
                file.close()
        else:
            print '网络状态异常'

    def getDiscription(self):
        print 'size %d' % len(self.heros)
        for hero in self.heros:
            url = "http://www.dota2.com.cn/hero/%s/" % hero
            print 'url', url
            req = requests.get(url, headers=self.headers)
            print 'req status_code:%d' % req.status_code
            if req.status_code == 200:
                soup = BeautifulSoup(req.content, 'html.parser')
                print 'title:%s' % soup.title.string
            else:
                print '网络状态异常'

    def start(self):
        baseUrl = "http://www.dota2.com.cn/heroes/"
        self.getHeroNames(baseUrl)
        self.getDiscription()


dota2 = Dota2()
dota2.start()
