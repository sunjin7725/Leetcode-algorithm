# -*- coding: utf-8 -*-  
""" 
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:


The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

Custom Judge:

The inputs to the judge are given as follows (your program is not given these inputs):

intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
listA - The first linked list.
listB - The second linked list.
skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.

Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
- Note that the intersected node's value is not 1 because the nodes with value 1 in A and B (2nd node in A and 3rd node in B) are different node references. In other words, they point to two different locations in memory, while the nodes with value 8 in A and B (3rd node in A and 4th node in B) point to the same location in memory.
"""
from typing import Optional


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


headA = ListNode(val=2, next=ListNode(val=6, next=ListNode(val=4, next=None)))
headB = ListNode(val=1, next=ListNode(val=5, next=None))


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        headA_cnt = 0
        headB_cnt = 0
        next_headA = headA
        next_headB = headB

        while next_headA:
            headA_cnt += 1
            next_headA = next_headA.next

        while next_headB:
            headB_cnt += 1
            next_headB = next_headB.next

        diff_cnt = abs(headA_cnt - headB_cnt)
        if headA_cnt <= headB_cnt:
            small_head = 'A'
        else:
            small_head = 'B'

        cnt = 0
        if small_head == 'A':
            while headA:
                if cnt < diff_cnt:
                    headB = headB.next
                    cnt += 1
                    continue
                if id(headA) == id(headB):
                    return headA
                headA = headA.next
                headB = headB.next

        if small_head == 'B':
            while headA:
                if cnt < diff_cnt:
                    headA = headA.next
                    cnt += 1
                    continue
                if id(headA) == id(headB):
                    return headA
                headA = headA.next
                headB = headB.next