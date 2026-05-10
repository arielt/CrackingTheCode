# Given a linked list, determine if it has a cycle in it.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # 95/14 solution - use set to map nodes
    def hasCycleSet(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        visited = set()
        
        while head:
            if head in visited:
                return True
            visited.add(head)
            head = head.next
            
        return False
    
    # 95/34 solution with 2 pointers
    def hasCycle(self, head):
        if not (head and head.next):
            return False
        slow = head
        fast = head.next
        
        while slow != fast:
            if not (fast and fast.next): return False
            slow = slow.next
            fast = fast.next.next
        
        return True

