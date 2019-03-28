#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin

nums = [1,2,3,4,5,1]
val =1
i = 0
while i < len(nums):
    if nums[i]==val:
        nums.remove(nums[i])
        i-=1
    i+=1
return len(nums)
