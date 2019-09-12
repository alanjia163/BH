#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin


'''
输出
输出结果


样例输入
5
1 2 3 2 1
5
3 2 1 4 7
样例输出
3
'''

def result_len(str1,str2) :
    l1 = len(str1)
    l2 = len(str2)
    resu = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]
    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            if str1[i - 1] == str2[j - 1]:
                resu[i][j] = resu[i - 1][j - 1] + 1
    return max(max(row) for row in resu)
n=input()
str1=list(map(int,input().split(" ")))
m=input()
str2=list(map(int,input().split(" ")))

print(str2,type(str2))
print(result_len(str1,str2))