# Swap Nodes in Pairs
# Given a linked list, swap every two adjacent nodes and return its head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        if not head.next:
            return head
        
        t = head
        dummy = head
        head = head.next
        
        while t:
            f = t
            s = t.next
            
            if not s:
                t = None
                dummy.next = f
            else:
                t = s.next
                s.next = f
                dummy.next = s
            f.next = t
            dummy = f
        
        return head

