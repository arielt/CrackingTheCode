// https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

#include <vector>

using namespace std;

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:

    TreeNode* bs(vector<int>& nums, int s, int e) {
        if (s > e) {
            return nullptr;
        }

        int m = (s + e) / 2;

        TreeNode* root = new TreeNode(nums[m]);
        root->left = bs(nums, s, m - 1);
        root->right = bs(nums, m + 1, e);

        return root;
    }

    TreeNode* sortedArrayToBST(vector<int>& nums) {
        return bs(nums, 0, nums.size() - 1);
    }
};
