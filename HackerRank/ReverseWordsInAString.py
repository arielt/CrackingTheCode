# Reverse Words in a String
# Input: "the sky is blue"
# Output: "blue is sky the"

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        res = ''
        i = len(words)
        prepend = False
        
        while i > 0:
            if prepend:
                res += ' '
            prepend = True
            
            res += words[i - 1]
            i -= 1
        
        return res

