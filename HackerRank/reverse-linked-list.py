# Reverse a singly linked list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseListIt(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        rv = None
        nxt = None
        
        while head:
            nxt = head.next
            head.next = rv
            rv = head
            head = nxt
        
        return rv
    
    def reverseListRec(self, head, prev):
        if not head:
            return prev
        
        nxt = head.next
        head.next = prev
        return self.reverseListRec(nxt, head)
    
    def reverseList(self, head):
        return self.reverseListRec(head, None)

