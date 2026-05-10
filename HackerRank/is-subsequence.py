# Given a string s and a string t, check if s is subsequence of t.

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ls = len(s)
        if ls == 0:
            return True
    
        lt = len(t)
        j = 0
        
        for i in range(lt):
            if t[i] == s[j]:
                j += 1
            if j == ls:
                return True
        
        return False

