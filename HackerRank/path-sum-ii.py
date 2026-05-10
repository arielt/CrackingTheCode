# Given a binary tree and a sum, find all root-to-leaf paths where each
# path's sum equals the given sum.

# Note: A leaf is a node with no children.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root, path, sum):
        if root:
            path.append(root.val)
            if root.val == sum and not (root.left or root.right):
                self.rv.append(path[:])
            self.dfs(root.left, path, sum - root.val)
            self.dfs(root.right, path, sum - root.val)
            path.pop()
    
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.rv = []
        self.dfs(root, [], sum)
        return self.rv

