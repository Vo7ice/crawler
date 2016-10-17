# -*- coding:utf-8 -*-
import json


def trans():
    with open('heros.json','r') as f:
        jsont_str = json.dumps(f)
        data = json.loads(jsont_str)
        print 'data:%s' % data.keys()
        
if __name__ == '__main__':
    trans()
    