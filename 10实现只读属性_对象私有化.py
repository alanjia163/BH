#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin
'''
实现只读属性
'''


class Person(object):
    def __init__(self, x):
        self._age = 20

    def get_age(self):
        return self._age


a = Person(20)
print(a.get_age())

a._age = 10
print(a.get_age())

'''
利用@property
#以访问属性的方式来访问 weight 方法
'''


class Mycls(object):
    _weight = 50

    # 以访问属性的方式来访问 weight 方法
    @property
    def get_weight(self):
        return self._weight


new_mycls = Mycls()
print(new_mycls.get_weight)
new_mycls.get_weight = 100
print(new_mycls.get_weight)
