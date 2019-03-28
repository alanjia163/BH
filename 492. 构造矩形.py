#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin


def constructRectangle(area: int):
    lw = []
    if area==1:
        return [1,1]
    for w in range(1,area):
        if area%w ==0:
            l =area/w
            if w * l == area and w <= l:
                lw.append(w)
    W = max(lw)
    L = area // W
    return [L, W]


if __name__ == '__main__':
    print(constructRectangle(1))
