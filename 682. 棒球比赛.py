#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin


def cal_point(ops):
    l =[]
    for i in range(len(ops)):
        if ops[i] == 'D':
            l.append(l[len(l)-1] * 2)
        elif ops[i] == '+':
            if len(l)>1:
                l.append(l[len(l)-1] + l[len(l) - 2])
            elif len(l)>0:
                l.append( l[len(l)-1])
        elif ops[i] == 'C':
            l.pop(len(l)-1)
            #l[i - 1] = 0
            #l.append(0)
        else:
            l.append(int(ops[i]))

    return sum(l)


if __name__ == '__main__':
    a = ["5", "2", "C", "D", "+"]
    print(cal_point(a))
