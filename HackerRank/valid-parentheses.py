# Given a string containing just the characters '(', ')', '{', '}', '['
# and ']', determine if the input string is valid.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        chars = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        stack = []
        
        for i in s:
            if (stack and chars.has_key(i) and stack[-1] == chars[i]):
                stack.pop()
            else:
                stack.append(i)
        
        if stack:
            return False
        
        return True

