#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin

# 独写了一个求下一个报数结果的方法：nextseq
# 用res表示要返回的报数。
def nextseq(seq):
    if len(seq) == 1:
        return '1' + seq
    res = ''
    count = 1
    for i in range(len(seq) - 1):
        if seq[i] == seq[i + 1]:
            count += 1
        else:
            res = res + str(count) + seq[i]
            count = 1
        if i == len(seq) - 2:  # 判断是否到达最后一个
            res = res + str(count) + seq[i + 1]
    return res


def countAndSay(n):
    List = []
    List.append('1')
    for i in range(1, n):
        cur = nextseq(List[i - 1])
        List.append(cur)
    return List[n-1]
a = countAndSay(4)
print(a)


