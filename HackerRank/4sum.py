# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        rv = []
        n = len(nums)
        nums.sort()

        print(nums)

        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n-2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                l = j + 1
                r = n - 1
            
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]

                    if s < target:
                        l += 1
                    elif s > target:
                        r -= 1
                    else:
                        rv.append([nums[i], nums[j], nums[l], nums[r]])
                
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                    
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1

                        l += 1
                        r -= 1
        
        return rv
                
