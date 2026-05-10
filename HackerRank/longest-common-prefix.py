# Longest Common Prefix
# Write a function to find the longest common prefix string amongst an
# array of strings.
# If there is no common prefix, return an empty string "".

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        res = ''
        i = 0
        
        for i in range(len(strs[0])):
            c = strs[0][i]
            
            for j in range(1, len(strs)):
                if len(strs[j]) <= i or strs[j][i] != c:
                    return res
            
            res += c
        
        return res
        

