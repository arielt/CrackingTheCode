# Merge k sorted linked lists and return it as one sorted list.
# first solution was 55.23% / 21.21%
# this one 84%/50%

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists or len(lists) == 0:
            return

        # initialize heap
        h = []
        for e in lists:
            if e:
                heapq.heappush(h, (e.val, e))

        rv = last = ListNode(0) # dummy node
        
        while len(h) > 0:
            (val, node) = heapq.heappop(h)
            last.next = node
            last = last.next
            node = node.next
            if node:
                heapq.heappush(h, (node.val, node))
                
        return rv.next

