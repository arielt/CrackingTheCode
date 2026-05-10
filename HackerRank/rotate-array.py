# Given an array, rotate the array to the right by k steps, where k is non-negative.

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        l = len(nums)
                
        # truncate unnecessary rotation steps
        k = k % l
        
        # reverse the whole list
        nums[:] = nums[:][::-1]
        
        # reverse first k 
        nums[:k] = nums[:k][::-1]
        
        # reverse the rest of the list
        nums[k:] = nums[k:][::-1]

