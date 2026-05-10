# Given an integer, write a function to determine if it is a power of two.

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0: return False
        
        while n > 1:
            if n % 2 != 0: return False
            n /= 2
        
        return True

