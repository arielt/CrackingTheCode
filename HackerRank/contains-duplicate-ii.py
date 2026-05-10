# Given an array of integers and an integer k, find out whether there 
# are two distinct indices i and j in the array such that nums[i] = 
# nums[j] and the absolute difference between i and j is at most k.

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dups = {}
        i = 0
        while i < len(nums):
            if dups.has_key(nums[i]):
                if i - dups[nums[i]] <= k:
                    return True
            dups[nums[i]] = i
            i += 1
        return False

