# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as:
#   a binary tree in which the left and right subtrees of every node differ in height by no more
#   than 1.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recCheck(self, node):
        if node is None:
            return 0
        
        l = self.recCheck(node.left)
        r = self.recCheck(node.right)
        
        if l == -1 or r == -1 or abs(l-r) > 1:
            return -1
        
        return max(l,r) + 1
            
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if self.recCheck(root) == -1:
            return False
        else:
            return True

