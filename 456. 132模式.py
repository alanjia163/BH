#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin

'''
思路应该是没有问题的,但是但是,,,,超出时间的现在 ...
'''


# def find132pattern(nums):
#     if len(nums)<3:
#         return False
#     if len(nums)==3:
#         if nums[0]<nums[2]<nums[1]:
#             return True
#         else:return False
#     for i in range(1,len(nums)-1):
#         lower = min(nums[:i])
#         if lower<nums[i]:
#             for k in range(i+1,len(nums)):
#                 if nums[k]<nums[i] and nums[k]>lower:
#                     return True
#     return False

    def find132pattern(nums):
        if len(nums) < 3:
            return False
        if len(nums) == 3:
            if nums[0] < nums[2] < nums[1]:
                return True
            else:
                return False
        lower = nums[0]
        for i in range(1, len(nums) - 1):
            if lower < nums[i]:
                for k in range(i + 1, len(nums)):
                    if nums[k] < nums[i] and nums[k] > lower:
                        return True
            else:
                lower = nums[i]
        return False


if __name__ == '__main__':
    print(find132pattern([-1, -2,3, 2, 0]))
