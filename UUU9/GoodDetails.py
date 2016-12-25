# coding=utf-8
import requests

__author__ = 'Vo7ice'


class GoodDetails(object):
    """
    收集Good的详情

    """

    def __init__(self, good):
        self.good = good
        self.good_id = good.get('oid')
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}

    def start(self):
        pass

    def get_detail(self, url):
        print 'start get hero %s detail.' % self.good.get('name')
        req = requests.get(url, headers=self.headers)
        print 'req status_code:%d' % req.status_code
        if req.status_code == 200:
            pass
        else:
            print 'network error'
