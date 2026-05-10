# Remove Nth Node From End of List
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return None
        
        size = 1
        c = p = head
        
        while c.next:
            if size > n:
                p = p.next
                
            c = c.next
            size += 1
        
        if size < n:
            return head
        
        if size == n:
            return head.next
        
        p.next = p.next.next
        return head

