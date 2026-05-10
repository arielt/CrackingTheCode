# Find K Pairs with Smallest Sums
# You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
# Define a pair (u,v) which consists of one element from the first array and one element from the second array.
# Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not (nums1 and nums2): return
        
        l1 = len(nums1)
        l2 = len(nums2)
        if l1 == 0 or l2 == 0: return
        
        pq = []
        visited = set()
        res = []
        
        heapq.heappush(pq, (nums1[0] + nums2[0], 0, 0))
        
        while len(res) < k and len(pq) > 0:
            (sum, i, j) = heapq.heappop(pq)
            
            if (i,j) in visited: continue
                
            visited.add((i,j))
            res.append((nums1[i], nums2[j]))
                       
            if (i + 1, j) not in visited and (i + 1) < l1:
                heapq.heappush(pq, (nums1[i + 1] + nums2[j], i + 1, j))
                     
            if (i, j + 1) not in visited and (j + 1) < l2:
                heapq.heappush(pq, (nums1[i] + nums2[j + 1], i, j + 1))
                
        return res

