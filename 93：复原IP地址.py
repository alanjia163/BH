#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin

def is_legal(a):
    if 0<=a<=255:




def restoreIpAddresses(s):
    """
    :type s: str
    :rtype: List[str]
    """
    if not s:
        return []
    def restore(s: str, remain: int):
        if remain == 1:
            if -1 < int(s) < 256 and str(int(s)) == s: #####如果s='01',则int(s)=1
                return [s]
            return []
        res = []
        if remain <= len(s) <= 3 * remain - 2:
            for i in restore(s[1:], remain - 1):
                res.append(s[:1] + '.' + i)
        if int(s[:2]) > 9 and remain + 1 <= len(s) <= 3 * remain - 1:
            for i in restore(s[2:], remain - 1):
                res.append(s[:2] + '.' + i)
        if 99 < int(s[:3]) < 256 and remain + 2 <= len(s) <= 3 * remain:
            for i in restore(s[3:], remain - 1):
                res.append(s[:3] + '.' + i)
        return res

    return restore(s, 4)


if __name__ == '__main__':
    s ='25525511135'
    result =restoreIpAddresses(s)
    print(result)
