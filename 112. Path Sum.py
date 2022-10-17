# -*- coding: utf-8 -*-  
""" 
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown
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
                                              left=None,
                                              right=TreeNode(val=1,
                                                             left=None,
                                                             right=None)
                                              )
                               )
                )


class Solution:
    def __init__(self):
        self.sum_list = []

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.find(root)
        print(self.sum_list)
        if targetSum in self.sum_list:
            return True
        return False

    def find(self, root, sum=0):
        if not root.left and not root.right:
            self.sum_list.append(sum + root.val)
            return
        sum += root.val
        if root.left: self.find(root.left, sum)
        if root.right: self.find(root.right, sum)

print(Solution().hasPathSum(root, 22))