# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recTree(self, root, level, res):
        if root is None:
            return
        if len(res) == level:
            res.append([])
        self.recTree(root.left, level+1, res)
        self.recTree(root.right, level+1, res)
        res[level].append(root.val)

    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.recTree(root, 0, res)
        res.reverse()
        return res

