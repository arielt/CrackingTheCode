# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero = 0
        
        for i in range(len(nums)):
            if nums[i]:
                nums[zero], nums[i] = nums[i], nums[zero]
                zero += 1
 
