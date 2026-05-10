# Minimum Operations to Make the Array Increasing

# You are given an integer array nums (0-indexed). In one operation, you can choose an element of the array 
# and increment it by 1.

# For example, if nums = [1,2,3], you can choose to increment nums[1] to make nums = [1,3,3].
# Return the minimum number of operations needed to make nums strictly increasing.

# An array nums is strictly increasing if nums[i] < nums[i+1] for all 0 <= i < nums.length - 1. An array of 
# length 1 is trivially strictly increasing.

# Test results

# Runtime: 108 ms, faster than 39.24% of Python online submissions for Minimum Operations to Make the Array 
# Increasing.

# Memory Usage: 14 MB, less than 77.91% of Python online submissions for Minimum Operations to Make the Array 
# Increasing.
class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = 0
        n = len(nums)
        i = 1
        
        while i < n:
            d = nums[i-1] - nums[i] + 1
            
            if d > 0:
                c += d
                nums[i] += d
            
            i+= 1
        
        return c

