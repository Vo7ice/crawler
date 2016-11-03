#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

logging.basicConfig(level=logging.INFO)
__author__ = 'Vo7ice'


class Model(dict):
    def __init__(self, **kwargs):
        super(Model, self).__init__(**kwargs)

    # 设置这个方法,可以通过对象.attr来访问属性
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    # 获得属性的值
    def getValue(self, key):
        return getattr(self, key, None)
