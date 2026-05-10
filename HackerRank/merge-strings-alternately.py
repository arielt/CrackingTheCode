# Merge Strings Alternately

# You are given two strings word1 and word2. Merge the strings by adding letters in 
# alternating order, starting with word1. If a string is longer than the other, append the 
# additional letters onto the end of the merged string.

# Return the merged string.

# Test results
# Runtime: 28 ms, faster than 15.56% of Python online submissions for Merge Strings 
# Alternately.
# Memory Usage: 13.5 MB, less than 65.23% of Python online submissions for Merge Strings 
# Alternately.
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        rv = ''
        l1 = len(word1)
        l2 = len(word2)
        
        for i in range(l1):
            rv += word1[i]
            if i < l2:
                rv += word2[i]
        
        i += 1
        while i < l2:
            rv += word2[i]
            i += 1
        
        return rv

