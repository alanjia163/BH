#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin

list = [1,2,3,4]
count =0
for i in list:
    for j in list:
        for k in list:
            if i !=j and k!=j and i !=k:
                count+=1
print(count)
count1=0
if __name__ == "__main__":
    s =  (1,2,3,4)
    for a in s:
        for b in s:
            for c in s:
                if a != b and b != c and c != a:
                    count1+=1
print(count1)