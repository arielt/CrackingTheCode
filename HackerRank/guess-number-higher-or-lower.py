# We are playing the Guess Game. The game is as follows:

# I pick a number from 1 to n. You have to guess which number I picked.

# Every time you guess wrong, I'll tell you whether the number is higher or lower.

# You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

# -1 : My number is lower
#  1 : My number is higher
#  0 : Congrats! You got it!

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessBound (self, l, r):
        g = (l+r) / 2
        a = guess(g)
        
        if a == 0:
            return g
        
        if a == -1:
            return self.guessBound(l, g-1)
        
        return self.guessBound(g+1, r)
        
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.guessBound(1, n)
        
