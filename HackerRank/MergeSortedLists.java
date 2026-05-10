/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0) return null;
        
        PriorityQueue<ListNode> q = new PriorityQueue<ListNode>((a,b) -> a.val - b.val);
        
        // init the queue
        for (int i = 0; i < lists.length; i++) {
            if (lists[i] != null) {
              q.add(lists[i]);
            }
        }
        
        if (q.isEmpty()) return null;
        ListNode curr = new ListNode(0); // dummy node
        ListNode rv = curr;
        
        while (!q.isEmpty()) {
            ListNode next = q.poll();
            curr.next = next;
            if (next.next != null) {
                q.add(next.next);
            }
            curr = curr.next;
        }
        
        return rv.next;
    }
}

