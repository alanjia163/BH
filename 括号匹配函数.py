#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin
def str_symbol_is_corre(s):
    symbol = 0
    dict1 = {'(': ')', '{': '}', '[': ']'}
    s_l = '({['
    s_r = ')}]'
    list1 = []
    count = 0
    for i in s:
        if count >= 0:
            if i in s_l:
                symbol += 1
                list1.insert(0, i)
                count += 1
            if i in s_r:
                symbol += 1
                if len(list1) > 0:
                    t = list1.pop(0)
                    if dict1[t] == i:
                        count -= 1
                    else:
                        return False
                else:
                    return False
        else:
            return False
    if count == 0:
        return True
    else:
        if symbol == 0:
            return True
        else:
            return False
str_symbol_is_corre('()[{}]')d