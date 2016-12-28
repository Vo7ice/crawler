# coding=utf-8
from bs4 import BeautifulSoup
import requests
from Config import base_url

__author__ = 'Vo7ice'


class SkillDetails(object):
    """
    收集Skill的详情

    """

    def __init__(self, skill):
        self.skill = skill
        self.skill_id = skill.get('oid')
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}

    def start(self):
        pass

    def get_detail(self, url):
        print 'start get skill %s detail.' % self.skill.get('name')
        req = requests.get(url, headers=self.headers)
        print 'req status_code:%d' % req.status_code
        if req.status_code == 200:
            soup = BeautifulSoup(req.content, 'html.parser')

        else:
            print 'network error'
