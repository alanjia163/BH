#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin

if __name__ == '__main__':
    X=3
    Y=4

    N=3
    lucky1=1
    lucky2=2
    lucky3=8
    lucky=[1,2,8]
    x_mag=[]#随机加入lucky
    y_mag=[]

    for i in lucky:
        if X-i in lucky:
            if i not in x_mag:
                x_mag.append(i)
            if X-i not in x_mag:
                x_mag.append(X - i)
        else:
            y_mag.append(i)

    print(x_mag)
    print(y_mag)


