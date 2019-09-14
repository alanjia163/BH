#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin

def solve(m):
    a = m
    n=4
    for i in range(1,n):
        a[i][0]=a[i-1][0]+m[i][0]
    for i in range(1,n):
        a[0][i]=a[0][i-1]+m[0][i]
    i=j=1
    print(a)
    while i < n:
        while j < n:
            top=m[i-1][j]
            left=m[i][j-1]
            a[i][j] = min(top,left ) + m[i][j]
            print(a[i][j]) #
            j+=1
        i+=1



if __name__ == '__main__':
    m = [[1, 3, 5, 9], [8, 1, 3, 4], [5, 0, 6, 1], [8, 8, 4, 0]]
    solve(m)
