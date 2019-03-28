#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin



def fourSum(nums, target):
    list_r = []
    for i in range(len(nums)):
        list_r.append(nums[i])
        for j in  range(i,len(nums)):
            list_r.append(nums[j])

            for k in  range(j,len(nums)):
                list_r.append(nums[k])

                for l in  range(k,len(nums)):
                    list_r.append(nums[l])
                    if sum(list_r) == target:
                        print(list_r)
                    # else:
         list_r= []


if __name__ == '__main__':
    fourSum([1, 0, -1, 0, -2, 2],0)