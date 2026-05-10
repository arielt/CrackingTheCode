# https://leetcode.com/problems/kth-largest-element-in-a-stream

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.h = nums
        heapq.heapify(self.h)
        while len(self.h) > self.k:
            heapq.heappop(self.h)

    def add(self, val: int) -> int:
        if len(self.h) < self.k:
            heapq.heappush(self.h, val)
        else:
            if val > self.h[0]:
                heapq.heappush(self.h, val)
                heapq.heappop(self.h)
        return self.h[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


