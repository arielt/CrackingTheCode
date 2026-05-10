/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    private ListNode mergeSort(ListNode a, ListNode b) {
        if (a == null) {
            return b;
        }
        
        if (b == null) {
            return a;
        }
        
        ListNode r;
        if (a.val > b.val) {
            r = b;
            r.next = mergeSort(a, b.next);
        } else {
            r = a;
            r.next = mergeSort(b, a.next);
        }
        
        return r;
    }
    
    private ListNode findMiddle(ListNode a) {
        if (a == null) {
            return null;
        }
        
        ListNode f = a.next;
        ListNode s = a;
        
        while (f != null) {
            f  = f.next;
            if (f != null) {
                f = f.next;
                s = s.next;
            }
        }
        
        return s;
    }
    
    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        
        ListNode m = findMiddle(head);
        ListNode mNext = m.next;
        m.next = null;
        
        ListNode l = sortList(head);
        ListNode r = sortList(mNext);
        
        return mergeSort(l, r);
    }
}
