# -*- coding: utf-8 -*-  
""" 
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(val=1,
                left=TreeNode(val=2,
                              left=None,
                              right=TreeNode(val=5,
                                             left=None,
                                             right=None)
                              ),
                right=TreeNode(val=3,
                               left=None,
                               right=None)
                )


class Solution:
    def __init__(self):
        self.path = []

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.find(root)
        return list(map(lambda x: '->'.join(map(str, x)), self.path))

    def find(self, root, prev_num=[]):
        if not root.left and not root.right:
            self.path.append(prev_num + [root.val])

        if root.left: self.find(root.left, prev_num + [root.val])
        if root.right: self.find(root.right, prev_num + [root.val])

print(Solution().binaryTreePaths(root))