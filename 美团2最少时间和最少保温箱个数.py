#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin

'''
输入
第一行包含 一个整数 n，(1<=n<=100) 表示保温箱的数量

第二行有 n 个正整数 a1,a2,…,an(1<=ai<=100)

ai表示第 i个保温箱的已有货物个数

第三行有 n 个正整数 b1,b2,…,bn(1<=bi<=100),bi 表示第 i 个保温箱的最大容量

显然,每一个ai<=bi

输出
输出为两个整数 k 和 t, k 表示能容纳所有货物的保温箱的最少个数,t 表示将所有货物转移到这 k 个保温箱所花费的最少时间,单位为秒.


样例输入
4
3 3 4 3
4 7 6 5
样例输出
2 6

提示
在样例一中,我们可以把第一个保温箱中的货物全部挪到第二个保温箱中,花费时间为 3 秒,此时第二个保温箱剩余容量为 1 ,然后把第四
个保温箱中的货物转移一份到第二个保温箱中,转移最后两份到第三个保温箱中.总花费时间也是 3 秒,所以最少保温箱个数是 2,最少花费时间为 6 秒
'''

def solve(n,list1,list2):
    num=0 #所需个数
    ti=0  #所需时间
    list3_can=[]#剩余可以装每个箱子
    total_value=0  #总份数
    sort_list2 =sorted(list2,reverse=True) #排序箱子容量
    for i in range(n):
        list3_can.append(list1[i]-list2[i])
        total_value+=list1[i]

    to_sov=0#已有容量
    while total_value>to_sov:
        to_sov+=sort_list2[num]
        num+=1
    print(num,sort_list2)
    print(to_sov)
    return num,ti

if __name__ == '__main__':
    n = int(input())
    list1 = list(map(int, input().split(" ")))
    list2 = list(map(int, input().split(" ")))
    print(solve(n, list1, list2))

