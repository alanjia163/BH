#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin

class Solution(object):
    def threeSum(self, nums,target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res=0
        nums.sort()
        length = len(nums)
        for i in range(length-2): #[8]
            if nums[i]>=target:
                break
            l,r=i+1,length-1 #[2]
            while l<r:
                total = nums[i]+nums[l]+nums[r]
                if total<target: #[3]
                    while l<r:
                        left = l
                        while left<r and nums[i]+nums[left]+nums[r]<target:
                            self.res+=1
                            left+=1
                        r-=1
                else:
                    r-=1
        return self.res

s=input()
arr=list(map(int,input().split(" ")))
k=int(input())
# arr=[-2,0,1,1,2,3,6]
# k=2
print(Solution().threeSum(arr, k))  # 6