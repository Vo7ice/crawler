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


class HeroSave(BaseSave):
    @property
    def name(self):
        return self.get('name')

    @name.setter
    def name(self, value):
        return self.set('name', value)

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
    def name(self):
        return self.get('name')

    @name.setter
    def name(self, value):
        return self.set('name', value)


class SkillSave(Object):
    @property
    def skill_id(self):
        return self.get('skill_id')

    @skill_id.setter
    def skill_id(self, value):
        return self.set('skill_id', value)

    @property
    def img_url(self):
        return self.get('img_url')

    @img_url.setter
    def img_url(self, value):
        return self.set('img_url', value)

    @property
    def skill_url(self):
        return self.get('skill_url')

    @skill_url.setter
    def skill_url(self, value):
        return self.set('skill_url', value)
