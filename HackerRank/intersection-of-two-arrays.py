# Intersection of Two Arrays
# Given two arrays, write a function to compute their intersection.

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s = None
        a = None
        rv = []
        
        if len(nums1) < len(nums2):
            s = set(nums1)
            a = nums2
        else:
            s = set(nums2)
            a = nums1
            
        for i in a:
            if i in s:
                rv.append(i)
                s.remove(i)

        return rv

