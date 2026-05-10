# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You may assume no duplicates in the array.
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while l < r:
            n = (l + r) / 2
            if nums[n] == target: return n
            if l + 1 == r:
                if target > nums[r]: return r + 1
                if target < nums[l]: return max(0, l - 1)
                return l + 1
            if target > nums[n]:
                l = n
            else:
                r = n
        if nums[l] == target: return l
        if target > nums[r]: return r + 1
        if target < nums[l]: return max(0, l - 1)
        return l + 1

