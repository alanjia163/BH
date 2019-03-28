#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin

'''
561. 数组拆分 I
'''
nums = [1,4,2,3]
nums.sort()
list1=nums[::2]
sum =0
for i in list1:
    sum += i
print(sum)


