class Solution(object):
    # recursive solution
    def findMinRec(self, nums, l, r):
        if l == r or nums[l] < nums[r]:
            return nums[l]
        
        if r-l < 2:
            return min(nums[l], nums[r])
        
        m = (l+r)/2
        if nums[m] > nums[r]:
            return self.findMinRec(nums, m, r)
        else:
            return self.findMinRec(nums, l, m)        
    
    # Runtime: O(logN), Space: O(1)
    def findMinNonRec(self, n):
        r = len(n) - 1
        if r == 0:
            return n[0]
        if r < 0:
            return None
        l = 0
        
        while l + 1 < r:
            m = (l+r)/2
            if (n[m] > n[r]):
                l = m
            else:
                r = m
        
        return min(n[l], n[r])

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return self.findMinRec(nums, 0, len(nums) - 1)
        # test cases: [], [1], [1,2,3], [3,1,2], [2,3,1]
        return self.findMinNonRec(nums)
        
