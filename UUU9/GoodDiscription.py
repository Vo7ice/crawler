# coding=utf-8

__author__ = 'Vo7ice'

import leancloud
from Model import GoodSave


class GoodDetail:
    global baseUrl

    def __init__(self):
        leancloud.init("tsVy6mtJMvQ1zhpnY4wdTVXo-gzGzoHsz", "gnJe9bgWGDfUaqaX5LQzyWHJ")
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
        baseUrl = "http://db.dota2.uuu9.com/"

    def getDetailInfo(self, url):
        pass

    def start(self):
        GoodSave = leancloud.Object.extend('GoodSave')
        query = GoodSave.query
        print 'list:%d' % (len(query))
        query.limit(10)
        skip = 0



detail = GoodDetail()
detail.start()
