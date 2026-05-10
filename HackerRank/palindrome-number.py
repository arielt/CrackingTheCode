# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is palindrome while 123 is not.

# Runtime: 56 ms, faster than 60.83% of Python online submissions
# Memory Usage: 13.2 MB, less than 90.75% of Python online submissions.


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        y = x
        r = 0

        while y > 0:
            t = y % 10
            r = r * 10 + t
            y = y / 10

        if x == r:
            return True

        return False

