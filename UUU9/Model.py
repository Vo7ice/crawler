#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from leancloud import Object

logging.basicConfig(level=logging.INFO)
__author__ = 'Vo7ice'


# 基础类 包含href(url) oid(id) img_src(图片) name(名字)
class BaseSave(Object):
    @property
    def href(self):
        return self.get('href')

    @href.setter
    def href(self, value):
        return self.set('href', value)

    @property
    def oid(self):
        return self.get('oid')

    @oid.setter
    def oid(self, value):
        return self.set('oid', value)

    @property
    def img_src(self):
        return self.get('img_src')

    @img_src.setter
    def img_src(self, value):
        return self.set('img_src', value)

    @property
    def name(self):
        return self.get('name')

    @name.setter
    def name(self, value):
        return self.set('name', value)


# 英雄存储类 包含nickname(别称) skill(技能) recommend(推荐装备)
class HeroSave(BaseSave):
    @property
    def nickname(self):
        return self.get('nickname')

    @nickname.setter
    def nickname(self, value):
        return self.set('nickname', value)

    @property
    def skill(self):
        return self.get('skill')

    @skill.setter
    def skill(self, value):
        return self.set('skill', value)

    @property
    def recommend(self):
        return self.get('recommend')

    @recommend.setter
    def recommend(self, value):
        return self.set('recommend', value)


# 物品存储类 包含gold(金钱) composite(合成公式) advanced(可合成装备)
class GoodSave(BaseSave):
    @property
    def gold(self):
        return self.get('gold')

    @gold.setter
    def gold(self, value):
        return self.set('gold', value)

    @property
    def composite(self):
        return self.get('composite')

    @composite.setter
    def composite(self, value):
        return self.set('composite', value)

    @property
    def advanced(self):
        return self.get('advanced')

    @advanced.setter
    def advanced(self, value):
        return self.set('advanced', value)

    @property
    def discription(self):
        return self.get('discription')

    @discription.setter
    def discription(self, value):
        return self.set('discription', value)

    @property
    def red(self):
        return self.get('red')

    @red.setter
    def red(self, value):
        return self.set('red', value)

    @property
    def yellow(self):
        return self.get('yellow')

    @yellow.setter
    def yellow(self, value):
        return self.set('yellow', value)

    @property
    def orange(self):
        return self.get('orange')

    @orange.setter
    def orange(self, value):
        return self.set('orange', value)

    @property
    def suit(self):
        return self.get('suit')

    @suit.setter
    def suit(self, value):
        return self.set('suit', value)

    # 0为基础物品 1为升级物品 2为神秘商店 3为roshan
    @property
    def source(self):
        return self.get('source')

    @source.setter
    def source(self, value):
        return self.set('source', value)

    """
    0:消耗品
    1：属性
    2：军备
    3：奥术
    4：普通
    5：辅助
    6：法器
    7：武器
    8：防具
    9：圣物
    10：神秘
    """

    @property
    def category(self):
        return self.get('category')

    @category.setter
    def category(self, value):
        return self.set('category', value)


# 物品存储类
class SkillSave(BaseSave):
    @property
    def hero_id(self):
        return self.get('hero_id')

    @hero_id.setter
    def hero_id(self, value):
        return self.set('hero_id', value)
