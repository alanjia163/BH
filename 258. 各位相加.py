#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin
'''
题目说的不清楚,是说返回最后相加后得到的个位数
'''
def addDigits(num: int) -> int:
    if num < 10:
        return num
    s = str(num)
    while len(s) >= 2:
        sum = 0
        for i in s:
            sum += int(i)
        s = str(sum)
    else:
        return int(s)




if __name__ == '__main__':
    print(addDigits(11))