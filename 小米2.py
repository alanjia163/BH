#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Jia ShiLin

def solve(list1):
    maxsum = 0
    tmp_value = 0
    for i in range(len(list1)):
        if tmp_value <= 0:
            tmp_value = list1[i]
        else:
            tmp_value += list1[i]
        if (tmp_value > maxsum):
            maxsum = tmp_value
    return maxsum

if __name__ == '__main__':
    list1 = list(map(int, input().split(" ")))
    result = solve(list1)
    print(result)
