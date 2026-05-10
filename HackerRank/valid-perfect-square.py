# Given a positive integer num, write a function which returns True if num is a perfect square else False.

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True

        l,r = 1, num/2
        
        while l <= r:
            m = (l + r) / 2
            sq = m*m
            
            if sq == num:
                return True
            
            if sq > num:
                r = m -1
            else:
                l = m + 1
        
        return False

