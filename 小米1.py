#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin

def solve(prices):

    if len(prices) <= 1:
        return 0
    pre = prices[0]
    tail = prices[0]
    maxProfit = 0
    for i in range(1, len(prices)):  # 从第二个元素开始访问数组
        if prices[i] - pre < 0:  # 替换头指针和尾指针为当前访问到的数组的最小值
            pre = prices[i]
            tail = prices[i]
        if prices[i] - pre > tail - pre:  # 替换尾指针为当前访问（从最小数值开始）的最大值
            maxProfit = max(prices[i] - pre, maxProfit)  # 对比此时利润和之前保存的最大利润，返回现阶段可获得的最大利润
            two =min(prices[i] - pre, maxProfit)
            tail = prices[i]
    return maxProfit+two


if __name__ == '__main__':
    list1 = list(map(int, input().split(" ")))
    result = solve(list1)
    print(result)