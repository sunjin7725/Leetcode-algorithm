# -*- coding: utf-8 -*-  
""" 
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(val=5,
                left=TreeNode(val=4,
                              left=TreeNode(val=11,
                                            left=TreeNode(val=7,
                                                          left=None,
                                                          right=None),
                                            right=TreeNode(val=2,
                                                           left=None,
                                                           right=None)
                                            ),
                              right=None),
                right=TreeNode(val=8,
                               left=TreeNode(val=13,
                                             left=None,
                                             right=None),
                               right=TreeNode(val=4,
                                              left=TreeNode(val=5,
                                                            left=None,
                                                            right=None),
                                              right=TreeNode(val=1,
                                                             left=None,
                                                             right=None)
                                              )
                               )
                )

class Solution:
    def __init__(self):
        self.path_list = []

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.find(root, targetSum)
        print(self.path_list)

    def find(self, root, target_num, prev_num=[]):
        if not root.left and not root.right:
            if target_num == sum(prev_num) + root.val:
                self.path_list.append(prev_num + [root.val])
            return
        if root.left:
            self.find(root.left, target_num, prev_num + [root.val])
        if root.right:
            self.find(root.right, target_num, prev_num + [root.val])


Solution().pathSum(root, 22)