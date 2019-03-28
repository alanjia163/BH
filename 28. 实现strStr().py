#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin

def strStr(haystack: str, needle: str) -> int:
    '''
    :param haystack:
    :param needle:
    :return: int
    '''
    i = 0
    j = 0
    lens = len(needle)
    if needle == '':
        return 0
    if not needle:
        return -1

    while i < len(haystack):
        if haystack[i:i + lens] == needle:
            return i
        i += 1
    return -1

c=strStr('bbbbbaba', 'ab')

print(c)
