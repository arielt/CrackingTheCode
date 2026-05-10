# Task
# Given a 0-indexed integer array nums, return true if it can be made strictly increasing after removing exactly one element, or false otherwise. If the array is already strictly increasing, return true.

# The array nums is strictly increasing if nums[i - 1] < nums[i] for each index (1 <= i < nums.length).

# Test results
# Runtime: 24 ms, faster than 100.00% of Python online submissions for Remove One Element to Make the Array Strictly Increasing.
# Memory Usage: 13.4 MB, less than 88.79% of Python online submissions for Remove One Element to Make the Array Strictly Increasing.

class Solution(object):
    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        index = 0
        count = 0
        n = len(nums)
        
        for i in range(n-1):
            if nums[i] >= nums[i+1]:
                index = i
                count += 1
        
        if count == 0:
            return True
        
        if count == 1:
            if index == 0 or index == n-2:
                return True
            if nums[index-1] < nums[index+1] or (index < n - 2 and nums[index] < nums[index + 2]):
                return True
            
        return False

