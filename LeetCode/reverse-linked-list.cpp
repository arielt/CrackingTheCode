// https://leetcode.com/problems/reverse-linked-list/description/

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
    ListNode* reverseList(ListNode* head) {
        // prev points to already reversed list
        // head points to a not reversed yet
        ListNode* prev = nullptr;
        ListNode* temp;

        while (head) {
            temp = head->next;
            head->next = prev;
            prev = head;
            head = temp;
        }

        return prev;
    }
};
