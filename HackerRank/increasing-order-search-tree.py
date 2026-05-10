# Increasing Order Search Tree
# Given a binary search tree, rearrange the tree in in-order so that the 
# leftmost node in the tree is now the root of the tree, and every node # has no left child and only 1 right child.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recIncBst(self, root, rv):
        if root is None: return
        self.recIncBst(root.left, rv)
        rv.append(root.val)
        self.recIncBst(root.right, rv)

    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        rv = []
        self.recIncBst(root, rv)
        dummy = curr = TreeNode(0)
        for n in rv:
            curr.right = TreeNode(n)
            curr = curr.right
            
        return dummy.right

