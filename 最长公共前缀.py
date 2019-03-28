#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin
\

# 方法一和二的思想一样
# 方法一
s_list = ['abbba', 'abbsb', 'acccccccccccc', 'abbbbbbbbbbbac']
s_list.sort(key=lambda x: len(x))

shot_str = s_list[0]
shot_len = len(s_list[0])

for i in range(shot_len):
    for s in s_list:
        if s[i] != shot_str[i]:
            return shot_str[:i]


# 方法(⊙o⊙)二
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        len_strs = len(strs)
        str_minlen = len(strs[0])
        for i in range(0, len_strs):  # 算出此数组中最短的那个字符串的长度
            if len(strs[i]) < str_minlen:
                str_minlen = len(strs[i])
        answer = ""
        for i in range(0, str_minlen):
            target = strs[0][i]  # 取第一个字符串的第i个字母作为比对的标准
            for j in range(0, len_strs):  # 对每一个字符串的第i个字母进行比对
                if strs[j][i] != target:
                    return answer
            answer = answer + target
        return answer
