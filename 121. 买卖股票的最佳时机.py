#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin

#a = [7,1,5,3,6,4]
#方法一:两层循环记录
a=[5,4,3,2,1]
def maxProfit(prices):
    if not prices:
        return 0
    profit = []

    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            if prices[i]<prices[j]:
                    profit.append(prices[j]-prices[i])
    if not profit:
        return 0
    return max(profit)
print(maxProfit(a))


'''
题目要求
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
注意你不能在买入股票前卖出股票。
示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
思路一
是不是在最低点买入，最高点卖出收益最大？回答是肯定的，那么找到最低点，最高点，看看先后顺序，不合理，找第二高的点....不要把问题想复杂；我们就假设第一个点为最低点，同时也是最高点，从头开始移动最高点，同时记录每个点对应的收益，只留下最大的，如果移动到的点比最低点还低，是时候考虑换个最低点了，然后继续刚才的操作，最后得到的就是最大收益

作者：慧鑫coming
链接：https://www.jianshu.com/p/7bffb93efa12
来源：简书
简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。
'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Jia ShiLin

# 独写了一个求下一个报数结果的方法：nextseq
# 用res表示要返回的报数。
def nextseq(seq):
    if len(seq) == 1:
        return '1' + seq
    res = ''
    count = 1
    for i in range(len(seq) - 1):
        if seq[i] == seq[i + 1]:
            count += 1