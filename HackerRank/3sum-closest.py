# Given an array nums of n integers and an integer target,
# find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        diff = None
        nums.sort()

        for i in range(len(nums) - 2):
            l, r = i+1, len(nums) - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]

                if diff is None or abs(s - target) < abs(diff):
                    diff = target - s

                if diff == 0:
                    return target

                if s < target:
                    l += 1
                else:
                    r -= 1

        return target - diff

