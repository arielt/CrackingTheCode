# Task
# Given the root of a binary tree, return the postorder traversal of its nodes' values.

# Results
# Runtime: 32 ms, faster than 60.26% of Python3 online submissions for Binary Tree Postorder Traversal.
# Memory Usage: 14.2 MB, less than 44.09% of Python3 online submissions for Binary Tree Postorder Traversal.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recPostorderTraversal(self, root, rv):
        if root is None:
            return
        self.recPostorderTraversal(root.left, rv)
        self.recPostorderTraversal(root.right, rv)
        rv.append(root.val)
        
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        rv = []
        self.recPostorderTraversal(root, rv)
        return rv

