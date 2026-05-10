# Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        curr = 9
        prev = 1
        for i in range(2, min(11, n+1)):
            prev += curr
            curr *= (11 - i)
        return curr + prev
 
