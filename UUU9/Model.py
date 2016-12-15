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

    # 力量
    @property
    def ability(self):
        return self.get('ability')

    @ability.setter
    def ability(self, value):
        return self.set('ablity', value)

    # 敏捷
    @property
    def agility(self):
        return self.get('agility')

    @agility.setter
    def agility(self, value):
        return self.set('agility', value)

    # 智力
    @property
    def intelligence(self):
        return self.get('intelligence')

    @intelligence.setter
    def intelligence(self, value):
        return self.set('intelligence', value)

    # 消耗
    @property
    def consume(self):
        return self.get('consume')

    @consume.setter
    def consume(self, value):
        return self.set('consume', value)

    # 属性
    @property
    def attri(self):
        return self.get('attri')

    @attri.setter
    def attri(self, value):
        return self.set('attri', value)

    # 军备
    @property
    def arms(self):
        return self.get('arms')

    @arms.setter
    def arms(self, value):
        return self.set('arms', value)

    # 奥术
    @property
    def arcane(self):
        return self.get('arcane')

    @arcane.setter
    def arcane(self, value):
        return self.set('arcane', value)

    # 普通
    @property
    def normal(self):
        return self.get('normal')

    @normal.setter
    def normal(self, value):
        return self.set('normal', value)

    # 辅助
    @property
    def auxiliary(self):
        return self.get('auxiliary')

    @auxiliary.setter
    def auxiliary(self, value):
        return self.set('auxiliary', value)

    # 法器
    @property
    def instrument(self):
        return self.get('instrument')

    @instrument.setter
    def intrument(self, value):
        return self.set('instrument', value)

    # 武器
    @property
    def weapon(self):
        return self.get('weapon')

    @weapon.setter
    def weapon(self, value):
        return self.set('weapon', value)

    # 护甲
    @property
    def armor(self):
        return self.get('armor')

    @armor.setter
    def armor(self, value):
        return self.set('armor', value)

    # 圣物
    @property
    def holy(self):
        return self.get('holy')

    @holy.setter
    def holy(self, value):
        return self.set('holy', value)

    # 神秘商店
    @property
    def mystery(self):
        return self.get('mystery')

    @mystery.setter
    def mystery(self, value):
        return self.set('mystery', value)

    # 生命值
    @property
    def hp(self):
        return self.get('hp')

    @hp.setter
    def hp(self, value):
        return self.set('hp', value)

    # 法力值
    @property
    def mp(self):
        return self.get('mp')

    @mp.setter
    def mp(self, value):
        return self.set('mp', value)

    # 生命恢复
    @property
    def life_regeneration(self):
        return self.get('life_regeneration')

    @life_regeneration.setter
    def life_regeneration(self, value):
        return self.set('life_regeneration', value)

    # 法力恢复
    @property
    def mana_regeneration(self):
        return self.get('mana_regeneration')

    @mana_regeneration.setter
    def mana_regeneration(self, value):
        return self.set('mana_regeneration', value)

    # 防具
    @property
    def defense(self):
        return self.get('defense')

    @defense.setter
    def defense(self, value):
        return self.set('defense', value)

    # 魔抗
    @property
    def magic_resist(self):
        return self.get('magic_resist')

    @magic_resist.setter
    def magic_resist(self, value):
        return self.set('magic_resist', value)

    # 吸血
    @property
    def vampire(self):
        return self.get('vampire')

    @vampire.setter
    def vampire(self, value):
        return self.set('vampire', value)

    # 攻击力
    @property
    def damage(self):
        return self.get('damage')

    @damage.setter
    def damage(self, value):
        return self.set('damage', value)

    # 攻击速度
    @property
    def attack_speed(self):
        return self.get('attack_speed')

    @attack_speed.setter
    def attack_speed(self, value):
        return self.set('attack_speed', value)

    # 移动速度
    @property
    def move_speed(self):
        return self.get('move_speed')

    @move_speed.setter
    def move_speed(self, value):
        return self.set('move_speed', value)

    # roshan
    @property
    def roshan(self):
        return self.get('roshan')

    @roshan.setter
    def roshan(self, value):
        return self.set('roshan', value)

    # 圣物关口
    @property
    def sacred_mark(self):
        return self.get('sacred_mark')

    @sacred_mark.setter
    def sacred_mark(self, value):
        return self.set('sacred_mark', value)

    # 支援法衣
    @property
    def supportive_vestments(self):
        return self.get('supportive_vestments')

    @supportive_vestments.setter
    def supportive_vestments(self, value):
        return self.set('supportive_vestments', value)

    # 秘法圣所
    @property
    def arcane_sanctum(self):
        return self.get('arcane_sanctum')

    @arcane_sanctum.setter
    def arcane_sanctum(self, value):
        return self.set('arcane_sanctum', value)

    # 保护领地
    @property
    def protectorate(self):
        return self.get('protectorate')

    @protectorate.setter
    def protectorate(self, value):
        return self.set('protectorate', value)

    # 魅惑遗物
    @property
    def enchanted_artifacts(self):
        return self.get('enchanted_artifacts')

    @enchanted_artifacts.setter
    def enchanted_artifacts(self, value):
        return self.set('enchanted_artifacts', value)

    # 远古兵器
    @property
    def ancient_weapon(self):
        return self.get('ancient_weapon')

    @ancient_weapon.setter
    def ancient_weapon(self, value):
        return self.set('ancient_weapon', value)

    # 武器商人比泽
    @property
    def bezer(self):
        return self.get('bezer')

    @bezer.setter
    def bezer(self, value):
        return self.set('bezer', value)

    # 饰品商人希娜
    @property
    def sheena(self):
        return self.get('sheena')

    @sheena.setter
    def sheena(self, value):
        return self.set('sheena', value)

    # 奎尔瑟兰的密室
    @property
    def quelsey(self):
        return self.get('quelsey')

    @quelsey.setter
    def quelsey(self, value):
        return self.set('quelsey', value)

    # 奇迹古树
    @property
    def miracle_tree(self):
        return self.get('miracle_tree')

    @miracle_tree.setter
    def miracle_tree(self, value):
        return self.set('miracle_tree', value)

    # 黑市商人
    @property
    def black_marketeer(self):
        return self.get('black_marketeer')

    @black_marketeer.setter
    def black_marketeer(self, value):
        return self.set('black_marketeer', value)

    # 地精实验室
    @property
    def goblin_lab(self):
        return self.get('goblin_lab')

    @goblin_lab.setter
    def goblin_lab(self, value):
        return self.set('goblin_lab')

    # 地精商人
    @property
    def goblin_merchant(self):
        return self.get('goblin_merchant')

    @goblin_merchant.setter
    def goblin_merchant(self, value):
        return self.set('goblin_merchant', value)


# 物品存储类
class SkillSave(BaseSave):
    @property
    def hero_id(self):
        return self.get('hero_id')

    @hero_id.setter
    def hero_id(self, value):
        return self.set('hero_id', value)
