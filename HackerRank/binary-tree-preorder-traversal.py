# Task
# Given the root of a binary tree, return the preorder traversal of its nodes' values.

# Results
# Runtime: 32 ms, faster than 60.80% of Python3 online submissions for Binary Tree Preorder Traversal.
# Memory Usage: 14.2 MB, less than 43.49% of Python3 online submissions for Binary Tree Preorder Traversal.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recPreorder(self, root, rv):
        if (root is None):
            return
        
        rv.append(root.val)
        self.recPreorder(root.left, rv)
        self.recPreorder(root.right, rv)
        
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        rv = []
        self.recPreorder(root, rv)
        return rv

