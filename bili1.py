#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin

a = [444,55,30,20,1]
# a=eval(input())
def max_n(list1):
    list1 = [str(x) for x in list1]
    list1.sort(reverse=True)
    for i in range(len(list1) - 1):
        if len(list1[i]) > len(list1[i + 1]):
            if list1[i][len(list1[i + 1])] < list1[i + 1][-1]:
                list1[i], list1[i + 1] = list1[i + 1], list1[i]

    result =str('').join(x for x in list1)
    return result

print(max_n(a))
