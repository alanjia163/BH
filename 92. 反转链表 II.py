#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def reverseBetween(self, head, m, n):
        """
        首先把所有链表压入一个列表里，然后反转相应的位置。创建新的链表。
        :type head: ListNode
        :rtype: ListNode
        """
        if head ==None:
            return
        if m ==n:
            return head
        stack = []
        first = ListNode(0)
        print(first)
        while head:
            stack.append(head.val)
            head = head.next
        stack[m-1:n] = reversed(stack[m-1:n])
        res = first
        while stack:
            first.next = ListNode(stack.pop(0))
            first = first.next
        return res.next
