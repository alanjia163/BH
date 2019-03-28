#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin

# l=[12,3,4,5,5]
# print(l.count(5))
# print(l.index(5))
def searchInsert(nums, target) -> int:
    if target in nums:
        return nums.index(target)
    else:
        nums.append(target)
        nums.sort()
        return nums.index(target)



searchInsert([1, 3, 5, 6], 5)
