# Implement strStr()
# Return the index of the first occurrence of needle in haystack, or -1
# if needle is not part of haystack.

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l1 = len(haystack)
        l2 = len(needle)
        if l2 == 0:
            return 0
        
        for s in range (l1-l2+1):
            for i in range (l2):
                if haystack[s+i] != needle[i]:
                    break
                if i == l2-1:
                    return s
        return -1

