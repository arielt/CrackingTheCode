# Given a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = [(root, 1)]
        rv = []
        
        while stack:
            (node, level) = stack.pop()
            
            if node: # testing against None is better
                if level > len(rv):
                    rv.append(node.val)
                stack.append((node.left, level + 1))
                stack.append((node.right, level + 1))
                
        return rv

