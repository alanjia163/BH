#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Jia ShiLin

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Jia ShiLin

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    if l1 is None and l2 is None :
        return None
    new_list = ListNode(0)
    pre = new_list
    while l1 is not None and l2 is not None:
        if l1.val<l2.val:
            pre.next=l1
            l1 = l1.next
        else:
            pre.next=l2
            l2 = l2.next
        pre =pre.next
    if l1 is not None:
        pre.next = l1
    else:
        pre.next=l2
    return  new_list.next


mergeTwoLists([1, 2], [2, 3])


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    if l1 is None and l2 is None :
        return None
    new_list = ListNode(0)
    pre = new_list
    while l1 is not None and l2 is not None:
        if l1.val<l2.val:
            pre.next=l1
            l1 = l1.next
        else:
            pre.next=l2
            l2 = l2.next
        pre =pre.next
    if l1 is not None:
        pre.next = l1
    else:
        pre.next=l2
    return  new_list.next


mergeTwoLists([1, 2], [2, 3])
