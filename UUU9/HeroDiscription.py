# coding=utf-8
from bs4 import BeautifulSoup
import requests
from requests.adapters import HTTPAdapter

import leancloud
from Model import HeroSave
import HeroDetails
from Config import base_url

__author__ = 'Vo7ice'


class HeroDiscription:
    def __init__(self):
        leancloud.init("tsVy6mtJMvQ1zhpnY4wdTVXo-gzGzoHsz", "gnJe9bgWGDfUaqaX5LQzyWHJ")
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}

    def start(self):
        HeroSave = leancloud.Object.extend('HeroSave')
        query = leancloud.Query(HeroSave)
        query.limit(10)
        i = 0
        while i < 19:
            query.skip(10 * i)
            for x in query.find():
                # url = base_url + x.get('href')
                # print 'url:', url
                # self.getDetailInfo(url, good=x)
                detail = HeroDetails
                detail.start()
            i += 1
            print 'i:', i

        # detail = HeroDetails()
        # s = requests.Session()
        # s.mount('http://db.dota2.uuu9.com/', HTTPAdapter(max_retries=5))
        # s.mount('https://db.dota2.uuu9.com/', HTTPAdapter(max_retries=5))
        # s.keep_alive = False
        # detail.start()


if __name__ == '__main__':
    discription = HeroDiscription()
    discription.start()
