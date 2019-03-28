#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin
'''
在列表的前后补0
    flowerbed.insert(0,0)
    flowerbed.append(0)
'''
def can(flowerbed, n):
    count = 0
    flowerbed.insert(0,0)
    flowerbed.append(0)
    if len(flowerbed) > 2:
        for i in range(1,len(flowerbed) - 1 ):
            if flowerbed[i] == 0:
                if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                    count += 1
                    flowerbed[i] = 1


    if count >= n:
        return True
    else:
        return False


if __name__ == '__main__':
    print(can([1,0,0,0,1,0,0], 2))
