# Given a linked list, rotate the list to the right by k places, where k is non-negative.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # retun length and last element
    def length(self, head):
        c = 0
        last = head
        while head:
            c += 1
            last = head
            head = head.next
        return (c, last)
    
    def kth(self, head, k):
        rv = head
        while k:
            rv = rv.next
            k -= 1
        return rv

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        if k == 0:
            return head
        
        (l, last) = self.length(head)
        last.next = head
        
        head = self.kth(head, l - (k%l) - 1)
        temp = head
        head = head.next
        temp.next = None
        return head

