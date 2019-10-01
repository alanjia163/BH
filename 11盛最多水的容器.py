#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin

def return_max_water(list1):
    result=0
    i=0
    j=len(list1)-1
    while i <j:
        if list1[i]<list1[j]:
            result=max(result,(j-i)*list1[i])
            i+=1
        else:
            result=max(result,(j-i)*list1[j])
            j-=1
    return result


if __name__ == '__main__':
    list1=[1,8,6,2,5,4,8,3,7]
    print(return_max_water(list1))

