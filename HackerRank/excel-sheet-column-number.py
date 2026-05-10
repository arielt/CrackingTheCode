class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        rv = 0
        base = ord('A')
        for c in s:
            rv = rv * 26 + (ord(c) - base + 1)
        return rv

