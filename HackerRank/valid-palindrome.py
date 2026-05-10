# Valid Palindrome
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        b = 0
        e = len(s) - 1
        
        while b < e:
            if not s[b].isalnum():
                b += 1
                continue
            
            if not s[e].isalnum():
                e -= 1
                continue
            
            if (s[b].lower() != s[e].lower()):
                return False
            
            b += 1
            e -= 1
        
        return True

