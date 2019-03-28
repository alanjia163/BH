#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin


s = 'DCXXI'#'III'#'MCMXCIV'
dict1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
list3 = []
for i in s:
    list3.append(dict1[i])
sum = 0
j = 0
while j < len(list3) - 1:
    if list3[j] > list3[j + 1]:
        sum += list3[j]
        j += 1
    elif list3[j] ==list3[j+1]:
        sum = sum + list3[j + 1] + list3[j]
        j += 2
    else:
        sum = (sum + list3[j + 1] - list3[j])
        j += 2
if j == len(list3)-1:
    sum += list3[j]
print(sum)
