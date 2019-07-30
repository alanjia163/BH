#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode):
        res = []

        if root:
            res += self.inorderTraversal(root.left)
            res.append(root.val)
            res += self.inorderTraversal(root.right)
        return res

a =[1,2,3]
b =[4,5]

c =a+b
a.append(b)
print(c)
print(a)