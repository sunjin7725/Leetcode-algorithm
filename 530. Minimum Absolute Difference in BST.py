# -*- coding: utf-8 -*-  
""" 
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

example 1:
Input: root = [4,2,6,1,3]
Output: 1
"""

import numpy as np
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


test_root = TreeNode(val=236,
                     left=TreeNode(val=104,
                                   right=TreeNode(val=227, left=None, right=None)
                                   ),
                     right=TreeNode(val=701,
                                    right=TreeNode(val=911, left=None, right=None)
                                    )
                     )

test_root2 = TreeNode(val=236,
                      left=TreeNode(val=104,
                                    left=None,
                                    right=TreeNode(val=227,
                                                   left=None,
                                                   right=None
                                                   )
                                    ),
                      right=TreeNode(val=701,
                                     left=None,
                                     right=TreeNode(val=911,
                                                    left=None,
                                                    right=None)
                                     )
                      )


class Solution:
    def __init__(self):
        self.answer = float('inf')

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.find(root)
        return self.answer

    def find(self, root, prev_num=[]):
        if root is None: return
        if len(prev_num) > 0:
            self.answer = min(self.answer, min(list(map(lambda x: abs(x-root.val), prev_num))))
        self.find(root.left, prev_num + [root.val])
        self.find(root.right, prev_num + [root.val])


print(Solution().getMinimumDifference(test_root))
