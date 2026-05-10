# Given an array nums of n integers, are there elements a, b, c in nums
# such that a + b + c = 0? Find all unique triplets in the array
# which gives the sum of zero.

# Notice that the solution set must not contain duplicate triplets.

# Runtime: 696 ms, faster than 73.06% of Python online submissions for 3Sum.
# Memory Usage: 16.7 MB, less than 82.44% of Python online submissions


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rv = []
        if len(nums) < 3:
            return rv

        nums.sort()

        # print nums
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i+1, len(nums) - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]
                # print i,l,r,s

                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    rv.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1

        return rv

