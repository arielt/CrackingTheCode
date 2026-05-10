# Task
# ou are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) 
# that is a non-empty substring of num, or an empty string "" if no odd integer exists.
# A substring is a contiguous sequence of characters within a string.

# Results
# Runtime: 32 ms, faster than 97.78% of Python online submissions for Largest Odd Number in String.
# Memory Usage: 15.2 MB, less than 99.37% of Python online submissions for Largest Odd Number in String.

class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        odds = {
            '1': True,
            '3': True,
            '5': True,
            '7': True,
            '9': True
        }
        
        i = len(num) - 1
        
        while (i >= 0):
            if num[i] in odds:
                return num[0:i+1]
            i -= 1
        
        return ""

