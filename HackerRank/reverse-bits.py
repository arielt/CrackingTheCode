# Reverse bits of a given 32 bits unsigned integer.

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int('{:032b}'.format(n)[::-1],2)

