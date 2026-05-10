# Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

# If possible, output any possible result.  If not possible, return the empty string.

import collections

class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        n = len(S)
        t = []
        count = collections.Counter(S)
        for v,c in sorted(count.items(), key=lambda t: t[1]):
            if c > (n+1)/2:
                return ""
            t.extend(v * c)
        
        res = [None] * n
        res[::2] = t[n/2:]
        res[1::2] = t[:n/2]
        
        return "".join(res)

