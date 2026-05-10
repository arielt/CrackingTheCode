# Given the root of a binary tree, return all root-to-leaf paths in any order.
# A leaf is a node with no children.

# Runtime: 23 ms, faster than 35.30% of Python online submissions for Binary Tree Paths.
# Memory Usage: 13.3 MB, less than 83.03% of Python online submissions for Binary Tree Paths.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.rv = []

    def isLeaf(self, root):
        if not (root.left or root.right):
            return True
        else:
            return False

    def bt(self, root, path):
        if self.isLeaf(root):
            self.rv.append(path)
            return
        
        if root.left:
            self.bt(root.left, path + '->' + str(root.left.val))
        
        if root.right:
            self.bt(root.right, path + '->' + str(root.right.val))
    
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        self.rv = []
        self.bt(root, str(root.val))
        return self.rv

