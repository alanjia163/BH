#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin

def isOneBitCharacter(bits):
    i = 0
    while i < len(bits) - 1:
        if bits[i] == 0:
            i += 1
        else:
            i += 2
    if i == len(bits) - 1:
        return True
    else:
        return False



if __name__ == '__main__':
    print(isOneBitCharacter([0,0,1,0,0]))
