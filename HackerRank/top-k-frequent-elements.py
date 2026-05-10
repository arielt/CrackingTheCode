# Given a non-empty array of integers, return the k most frequent elements.

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 94.67% / 51.22% solution, python magic
        # c = collections.Counter(nums)
        # return heapq.nlargest(k, c.keys(), key=c.get)
        
        # a bit more classic solution, also more performant one: 94.69% / 90.24%
        c = {}
        for i in nums:
            if c.has_key(i):
                c[i] += 1
            else:
                c[i] = 1
        
        h = []
        for key in c:
            heapq.heappush(h, (c[key], key))
            if len(h) > k:
                heapq.heappop(h)
        
        res = []
        for i in h:
            res.append(i[1])
            
        return res

