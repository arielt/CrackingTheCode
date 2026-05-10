# Given two sorted arrays nums1 and nums2 of size m and n respectively,
# return the median of the two sorted arrays.

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0:
            raise InputError
            
        i_min, i_max, half_len = 0, m, (m + n + 1) // 2 # python 3 floor division
        while i_min <= i_max:
            i = (i_min + i_max) // 2
            j = half_len - i # j is derived from j
            
            if i < m and nums2[j-1] > nums1[i]: # i is too small, increase it
                i_min = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]: # is too big, decrease it
                i_max = i - 1
            else:
                if i == 0: max_of_left = nums2[j-1]
                elif j == 0: max_of_left = nums1[i-1]
                else: max_of_left = max(nums1[i-1], nums2[j-1])
                    
                if (m + n) %2 == 1: # odd number of elements
                  return max_of_left
            
                if i == m: min_of_right = nums2[j]
                elif j == n: min_of_right = nums1[i]
                else: min_of_right = min(nums1[i], nums2[j])
                
                return (max_of_left + min_of_right) / 2 # python 3 float division
