#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin

import unicodedata

#
# t = u'中国，中文，标点符号！你好？１２３４５＠＃【】+=-（）'
# t2 = unicodedata.normalize('NFKC', t)
# print(t2)


def chang_zh_to_en(path):
    f = open(path, 'r', encoding='utf-8')
    old = f.read()
    print(f.read())
    new = unicodedata.normalize('NFKC', old)
    print(old)
    print(new)

    f1 = open(path, 'w', encoding='utf-8')
    f1.write(new)
    f.close()
    f1.close()


if __name__ == '__main__':
    path = 'test1.py'
    chang_zh_to_en(path)
