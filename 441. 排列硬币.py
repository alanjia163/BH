#!/usr/bin/env python
# -*- coding:utf-8 -*- x
# Author: Jia ShiLin


def arrangeCoins(n: int) -> int:
    count = 0
    sum = 0
    if n == 1:
        return 1
    for i in range(1, n):
        sum += i
        if sum > n:
            break
        print('¤' * i)
        count = i
    return count


if __name__ == '__main__':
    print(arrangeCoins(5))
