#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin

def so(list1,list2):
    if list2 in list1:
        return 'SUB'
    i=0
    while i in range(len(list2)):
        t1=list2[i]
        t2=list1
        if list2[i] in list1:
            index =list1.find(list2[i])
            if index+1:
                list1 = list1[index + 1:]
                list2=list2[1:]
            else:
                return 'NO'
        else:
            return 'NO'
    if i==len(list2):
        return 'SUB'
if __name__ == '__main__':
    N=int(input())
    list1=[]
    list2=[]
    list3=[]
    i=0
    while i <N:
        list1=input()
        list2=input()
        i+=1
        list3.append(so(list1, list2))
    for i in list3:
        print(i)







