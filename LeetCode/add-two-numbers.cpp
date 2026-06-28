// https://leetcode.com/problems/add-two-numbers/

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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int c = 0; // carry over
        int s = 0; // sum
        ListNode dummy;
        ListNode * curr = &dummy;

        while (l1 || l2 || c) {
            s = c + (l1 ? l1->val : 0) + (l2 ? l2->val : 0);
            curr->next = new ListNode(s % 10);
            c = s / 10;
            curr = curr->next;
            
            if (l1) {
                l1 = l1->next;
            }

            if (l2) {
                l2 = l2->next;
            }
        }

        return dummy.next;        
    }
};
