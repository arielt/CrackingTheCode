# Check if Array Is Sorted and Rotated
# Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated 
# some number of positions (including zero). Otherwise, return false.

# There may be duplicates in the original array.

# Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % # A.length], where % is the modulo operation.

# Test results
# Runtime: 24 ms, faster than 50.37% of Python online submissions for Check if Array Is Sorted and Rotated.
# Memory Usage: 13.3 MB, less than 62.96% of Python online submissions for Check if Array Is Sorted and Rotated.

class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        c = 0
        l = len(nums)
        
        for i in range(l-1):
            if nums[i] > nums[i+1]:
                c += 1
            
        if nums[l-1] > nums[0]:
            c += 1
            
        if c < 2:
            return True
        return False

