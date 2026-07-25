// https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode dummy;        
        dummy.next = head;

        ListNode* p = &dummy;

        while(head && head->next) {
            if (head->val != head->next->val) {
                p = head;
            } else {
                while (head && head->next && (head->val == head->next->val)) {
                    head = head->next;
                }
                p->next = head->next;
            }
            head = head->next;
        }

        return dummy.next;
    }
};
