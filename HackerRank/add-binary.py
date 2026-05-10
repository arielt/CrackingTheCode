# Given two binary strings a and b, return their sum as a binary string.

# Runtime: 47 ms, faster than 5.05% of Python online submissions for Add Binary.
# Memory Usage: 13.4 MB, less than 94.16% of Python online submissions for Add 
# Binary.

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        la, lb = len(a), len(b) 
        l = max(la, lb)
        
        c, r = 0, ''
        
        for i in range(l):
            ia, ib = (la - i - 1), (lb - i - 1)

            ra = 0
            if ia >= 0:
                ra = a[ia]

            rb = 0
            if ib >= 0:
                rb = b[ib]
                
            add = int(ra) + int(rb) + c # sum digits and carry over
            if add > 1: # compute carry over
                c = 1
            else:
                c = 0
                
            r = r + str(add % 2)
        
        # last carry over
        if c:
            r = r + '1'
        
        return r[::-1]

