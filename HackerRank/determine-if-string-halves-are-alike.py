# Determine if String Halves Are Alike

# You are given a string s of even length. Split this string into two halves of equal lengths, and let a be 
# the first half and b be the second half.

# Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 
# 'U'). Notice that s contains uppercase and lowercase letters.

# Return true if a and b are alike. Otherwise, return false.


# Test results
# Runtime: 28 ms, faster than 55.04% of Python online submissions for Determine if String Halves Are Alike.
# Memory Usage: 13.4 MB, less than 92.76% of Python online submissions for Determine if String Halves Are 
# Alike.

class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        
        h = len(s)/2
        c1,c2 = 0,0
        for i in range(h):
            if s[i] in vowels:
                c1 += 1
            if s[i + h] in vowels:
                c2 += 1
        
        if c1 == c2:
            return True
        
        return False

