# Longer Contiguous Segments of Ones than Zeros

# Given a binary string s, return true if the longest contiguous segment of 1s is strictly longer than the 
# longest contiguous segment of 0s in s. Return false otherwise.

# For example, in s = "110100010" the longest contiguous segment of 1s has length 2, and the longest 
# contiguous segment of 0s has length 3.
# Note that if there are no 0s, then the longest contiguous segment of 0s is considered to have length 0. The 
# same applies if there are no 1s.

# Test results

# Runtime: 20 ms, faster than 69.55% of Python online submissions for Longer Contiguous Segments of Ones than Zeros.
# Memory Usage: 13.5 MB, less than 58.65% of Python online submissions for Longer Contiguous Segments of Ones than Zeros.
    
class Solution(object):
    def checkZeroOnes(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ones, max_ones = 0, 0
        zeroes, max_zeroes = 0, 0
        in_ones = False
        
        for a in s:
            if a == '1':
                if in_ones:
                    ones += 1
                else:
                    in_ones = True
                    ones = 1
                if ones > max_ones:
                    max_ones = ones
            elif a == '0':
                if in_ones:
                    in_ones = False
                    zeroes = 1
                else:
                    zeroes += 1
                if zeroes > max_zeroes:
                    max_zeroes = zeroes
            
        if max_ones > max_zeroes:
                return True
        
        return False

