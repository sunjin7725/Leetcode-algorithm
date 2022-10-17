# -*- coding: utf-8 -*-  
""" 
Given the root of a binary tree, invert the tree, and return its root.

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(val=4,
                left=TreeNode(val=2,
                              left=TreeNode(val=1,
                                            left=None,
                                            right=None),
                              right=TreeNode(val=3,
                                             left=None,
                                             right=None)
                              ),
                right=TreeNode(val=7,
                               left=TreeNode(val=6,
                                             left=None,
                                             right=None),
                               right=TreeNode(val=9,
                                              left=None,
                                              right=None)
                               )
                )

def dfs(root, result_root=TreeNode()):
    if root is None: return
    result_root.val = root.val
    if root.left:
        result_root.right = TreeNode()
        dfs(root.left, result_root.right)
    if root.right:
        result_root.left = TreeNode()
        dfs(root.right, result_root.left)

result_root = TreeNode()
dfs(root, result_root)
print(result_root)
