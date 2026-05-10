# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding
# up all the values along the path equals the given sum

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        
        if root.left is None and root.right is None: # leaf
            if sum == root.val:
                return True
            return False
        
        return (self.hasPathSum(root.left, sum - root.val) or
               self.hasPathSum(root.right, sum - root.val))

