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
        
        p = head
        
        while p.next:
            p.val, p.next.val = p.next.val, p.val
            p = p.next.next
            if not p:
                break
                
        return head

