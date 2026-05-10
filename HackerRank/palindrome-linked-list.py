# Given a singly linked list, determine if it is a palindrome.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def size(self, head):
        size = 0
        while head:
            size += 1
            head = head.next
        return size
    
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head: return True
        
        s = self.size(head)
        if s == 1:
            return True
        
        go = s/2
        prev, forw = None, None
        curr = head
        for i in range(go):
            forw = curr.next
            curr.next = prev
            prev = curr
            curr = forw
        
        forw = curr
        curr = prev
        
        if s % 2 == 1:
            forw = forw.next
        
        while forw:
            if forw.val != curr.val:
                return False
            forw = forw.next
            curr = curr.next
        
        return True

