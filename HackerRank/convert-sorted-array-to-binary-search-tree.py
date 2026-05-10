# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0: return
        mid = len(nums)/2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[0:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
        
