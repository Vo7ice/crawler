#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from leancloud import Object

logging.basicConfig(level=logging.INFO)
__author__ = 'Vo7ice'


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


class SkillSave(BaseSave):
    pass
