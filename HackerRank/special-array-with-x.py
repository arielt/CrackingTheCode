# You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.

# Notice that x does not have to be an element in nums.

# Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.

# solution: 99.83% speed, 53% memory
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        i  = len(nums) - 1
        
        nums.sort()        
        c = 1
        
        while i > 0:
            if nums[i-1] != nums[i]:
                if c <= nums[i] and c > nums[i-1]:
                    return c
            c += 1
            i -=1
                          
        if nums[0] >= c:
            return c
        else:
            return -1

