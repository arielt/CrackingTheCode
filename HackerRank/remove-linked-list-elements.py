# Remove Linked List Elements

# Remove all elements from a linked list of integers that have value val.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        # more elegant solution with first dummy node
        dummy = ListNode(None)
        dummy.next = head
        
        curr = head
        prev = dummy
        
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
            
        return dummy.next
        

    def removeElementsX(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # immediate solution
        prev = None
        rv = curr = head
        
        while curr:
            if curr.val == val:
                if prev is None:
                    rv = curr.next
                else:
                    prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        
        return rv

