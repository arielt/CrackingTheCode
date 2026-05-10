# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # mirrored traversal - root, left, right vs root, right, left
    # this is working recursive solution
    def isSymmetricRec(self, first, second):
        if first == None and second == None:
            return True
        if first == None or second == None:
            return False
        if first.val != second.val:
            return False
        return self.isSymmetricRec(first.left, second.right) and self.isSymmetricRec(first.right, second.left)
        

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # call to recursive solution
        # return self.isSymmetricRec(root, root)
        fq = [root]
        sq = [root]
        while len(fq) > 0:
            first = fq.pop()
            second = sq.pop()
            if first == None and second == None:
                continue
            if first == None or second == None:
                return False
            if first.val != second.val:
                return False
            fq.append(first.left)
            fq.append(first.right)
            sq.append(second.right)
            sq.append(second.left)
        if len(sq) > 0: return False
        return True

