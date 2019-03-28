#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin

class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        N = len(S)
        A = []
        o = 0
        j = N
        for i in range(N):
            if S[i] == 'I':
                A.append(o)
                o += 1

            elif S[i] == 'D':
                A.append(j)
                j -= 1
        A.append(j)
        return A
