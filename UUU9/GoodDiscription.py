# coding=utf-8
import time
from bs4 import BeautifulSoup
import requests
from requests.adapters import HTTPAdapter

__author__ = 'Vo7ice'

import leancloud
from Model import GoodSave


class GoodDetail:
    global baseUrl

    def __init__(self):
        leancloud.init("tsVy6mtJMvQ1zhpnY4wdTVXo-gzGzoHsz", "gnJe9bgWGDfUaqaX5LQzyWHJ")
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}

    def getDetailInfo(self, url, good):
        req = requests.get(url, headers=self.headers)
        print 'req status_code:%d' % req.status_code
        if req.status_code == 200:
            soup = BeautifulSoup(req.content, 'html.parser')
            span = soup.find_all('span', 'paddju')
            print 'span:%s' % span
            for index, p in enumerate(span):
                print 'index:%d,p:%s' % (index, p)
                if index == 0:
                    if p.string is None:
                        pass
                    else:
                        for a in p.findAll('a'):
                            pass
        else:
            print 'network error'

    def start(self):
        baseUrl = "http://db.dota2.uuu9.com/"
        GoodSave = leancloud.Object.extend('GoodSave')
        query = leancloud.Query(GoodSave)
        query.limit(10)
        good_info = query.find()[0]
        url = baseUrl + good_info.get('href')
        print 'url:%s' % url
        self.getDetailInfo(url, good=good_info)
        # skip = 0
        # for index, good in enumerate(query):
        #     href = good.get('href')
        #     url = baseUrl + href
        #     self.getDetailInfo(url, good_info=good)
        #     time.sleep(5)


detail = GoodDetail()
s = requests.Session()
s.mount('http://db.dota2.uuu9.com/', HTTPAdapter(max_retries=5))
s.mount('https://db.dota2.uuu9.com/', HTTPAdapter(max_retries=5))
s.keep_alive = False
detail.start()

"""
<div class="bord" style="padding: 10px;">
    <div class="skilltop skill cl">
        <div class="picbox l">
            <a href="/goods/show/ArcaneBoots">
                <img title="奥术鞋" src="http://dota2dbpic.uuu9.com/272885ab-41ee-4ca6-803c-975697efa6c3mifaxie.gif" /></a>
        </div>
        <div class="textbox r">
            <a href="javascript:void(0);" class="name">奥术鞋</a>
            <span class="paddju">
                <p>
                    分类：
                    <a href="/goods/list/?gts=2">法力值</a>
                    <a href="/goods/list/?gts=10">移动速度</a>
                    <a href="/goods/list/?gts=19">辅助</a>
                    <a href="/goods/list/?gts=4">法力回复</a>
                    <a href="/goods/list/?gts=27">支援法衣</a>
                </p>
                <p>
                    装备这种鞋子的法师在战斗中极具价值。
                    </br>    <span class="red">+250魔法</span>
                    </br>    <span class="red">+55移动速度</span>
                    </br>    <span class="red">主动：补充魔法</span>
                    </br>
                    </br>    <span class="yellow">补充魔法：</span>
                    </br>    <span class="yellow">回复附近友方单位135点魔法。</span>
                    </br>    <span class="yellow">作用范围：600  </span>
                    </br>    <span class="yellow">冷却时间：55s</span>
                    </br>
                    </br>    <span class="yellow">额外资料：</span>
                    </br>    <span class="yellow">可拆分。</span>
                    </br>    <span class="yellow">修补匠不能刷新该物品。</span>
                    </br>    <span class="yellow">移动速度提升不能和其他鞋类物品叠加。</span>
                </p>
            </span>
            <span class="paddju">
                <span class="price">总价格：
                    <span class="gold">1450</span>
                </span>
            </span>
        </div>
    </div>

    <div id="goodslist">
        <div class="anskill goods m-10">
        <div class="title">
            <h4>合成公式</h4>
        </div>
        <div class="content jianbg cl">
            <ul>
                <li class="cl">
                    <div class="picbox l">
                        <a href="/goods/show/BootsofSpeed">
                            <img gid="93" src="http://dota2dbpic.uuu9.com/434f4870-0ed2-4ef2-bfe3-baaee9dffa0bBoots_of_Speed.png" /></a>
                    </div>
                    <div class="text l">
                        <a href="/goods/show/BootsofSpeed">速度之靴</a><br />
                        <span class="gold">450</span>
                    </div>
                </li>
                <li class="cl">
                    <div class="picbox l">
                        <a href="/goods/show/EnergyBooster">
                            <img gid="62" src="http://dota2dbpic.uuu9.com/de8e11c7-3ebf-438a-acc7-47c36ca0139e1.jpg" /></a>
                    </div>
                    <div class="text l">
                        <a href="/goods/show/EnergyBooster">能量之球</a><br />
                        <span class="gold">1000</span>
                    </div>
                </li>
            </ul>
        </div>
    </div>

    <div class="anskill goods m-10">
        <div class="title">
            <h4>进阶合成物品</h4>
        </div>
        <div class="content jianbg cl">
            <ul>
                <li class="cl">
                    <div class="picbox l">
                        <a href="/goods/show/guardian GREAVES">
                            <img gid="205" src="http://dota2dbpic.uuu9.com/2347e493-49b3-4e23-b41d-ff22cecaf77b1.png" /></a>
                    </div>
                    <div class="text l">
                        <a href="/goods/show/guardian GREAVES">卫士胫甲</a><br />
                            <span class="gold">5300</span>
                        </div>
                </li>
            </ul>
        </div>
    </div>

</div>

<div class="belong m-10">
    <div class="title">
        <h4>适合这件道具的英雄</h4>
    </div>
    <div class="content jianbg">
        <ul class="cl" id="herolist">
            <li class="cl">
                <div class="headpic l">
                    <a hid="22" href="/hero/show/Tiny">
                        <img  src="http://dota2dbpic.uuu9.com/7da65f49-9894-4c0b-888b-00ce495cc909000.jpg" /><b></b></a>
                </div>
                <div class="heroname l">
                    <a href="/hero/show/Tiny"><b>山岭巨人</b></a><br />
                    <a href="/hero/show/Tiny">小小</a>
                </div>
            </li>
            <li class="cl">
                <div class="headpic l">
                    <a hid="20" href="/hero/show/ES">
                        <img  src="http://dota2dbpic.uuu9.com/8408006c-1f74-4bea-8685-739ab02b104800.jpg" /><b></b></a>
                </div>
                <div class="heroname l">
                    <a href="/hero/show/ES"><b>撼地者</b></a><br />
                    <a href="/hero/show/ES">雷格石蹄</a>
                </div>
            </li>
        </ul>
    </div>
</div>

"""
