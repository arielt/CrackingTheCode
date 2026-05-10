# Minimum Remove to Make Valid Parentheses
# Given a string s of '(' , ')' and lowercase English characters. 
# Your task is to remove the minimum number of parentheses ( '(' or ')',
# in any positions ) so that the resulting parentheses string is valid
# and return any valid string.

class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        rv = []
        stack = [] # track indices of opening brackets
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
                rv.append('')
            elif s[i] == ')':
                if (stack):
                    rv[stack[-1]] = '('
                    rv.append(')')
                    stack.pop()
                else:
                    rv.append('')
            else:
                rv.append(s[i]) # letter
        
        return ''.join(rv)
                

