#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin

def findContentChildren(g, s):
    count = 0
    g.sort()
    s.sort()
    t=0#用来记录下次,匹配的位置
    for i in range(len(s)):
        for j in range(t,len(g)):
            if g[j] <= s[i]:
                count += 1
                t=j+1
                break
    return count

if __name__ == '__main__':
    print(findContentChildren([10,9,8,7],[5,6,7,8]))