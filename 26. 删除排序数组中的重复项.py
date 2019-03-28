#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Jia ShiLin

def del_mul(nums):
    if nums is None:
        return None
    elif len(nums) == 1:
        return 1
    else:
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                nums.remove(nums[i])
                i -= 1
            i += 1
    print(nums)


del_mul([1, 1, 2])
