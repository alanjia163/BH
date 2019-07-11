#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin
'''
list_test=[1,3,4,5,7,8,10,13,14]
len(list_test)=9 
target=4
'''

list_test=[1,3,4,5,7,8,10,13,14]
# print(len(list_test))#  :9
target=4

def binarySearch(test,key,):
    n=len(test)
    low =0
    high=n

    while high>=low:
        mid = (high + low) //2
        print('index:%d，value:%d' % (mid,test[mid]))
        print(test[mid],key)

        if test[mid] == key:
            return mid
        elif test[mid] > key:
            high=mid-1
        else:
            low =mid+1
    return -1

if __name__ == '__main__':
    print(binarySearch(list_test,4,))




