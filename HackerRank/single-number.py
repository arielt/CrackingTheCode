# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rv = 0
        for n in nums:
            rv ^= n
        return rv

