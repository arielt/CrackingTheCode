# Given two strings s and t, determine if they are isomorphic.
# Two strings are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        tr = {}
        rev = {}
        for i,v in enumerate(s):
            if tr.has_key(v):
                if tr[v] != t[i]:
                    return False
            else:
                if rev.has_key(t[i]) and rev[t[i]] != v:
                    return False
                tr[v] = t[i]
                rev[t[i]] = v
        return True
        
