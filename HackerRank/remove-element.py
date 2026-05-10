# Remove Element

# Given an array nums and a value val, remove all instances of that
# value in-place and return the new length.

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = 0
        c = 0
        l = len(nums)
        while True:
            while n < l and nums[n] != val:
                n += 1
            if n == l:
                return n
            c = n + 1
            while c < l and nums[c] == val:
                c += 1
            if c == l:
                return n
            nums[n] = nums[c]
            nums[c] = val

