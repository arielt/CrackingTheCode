# Given a binary tree, return the tilt of the whole tree.

# The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values. Null node has tilt 0.

# The tilt of the whole tree is defined as the sum of all nodes' tilt.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def traverse(self, root):
        if (not root):
            return (0, 0)
        
        (lSum, lTilt) = self.traverse(root.left)
        (rSum, rTilt) = self.traverse(root.right)
        
        return (lSum + rSum + root.val, lTilt + rTilt + abs(lSum - rSum))
    
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if (not root):
            return 0
        
        (lSum, lTilt) = self.traverse(root.left)
        (rSum, rTilt) = self.traverse(root.right)

        return lTilt + rTilt + abs(lSum - rSum)

