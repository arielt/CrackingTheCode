# Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        els = path.split('/')
        
        for el in els:
            if el == '.' or el == '':
                continue
            if el == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(el)
        
        return '/' + '/'.join(stack)

