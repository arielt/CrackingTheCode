// https://leetcode.com/problems/validate-binary-search-tree

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
private:
    bool check(TreeNode* root, TreeNode* min, TreeNode* max) {
        if (!root) {
            return true;
        }

        if (min && (root->val <= min->val) || max && (root->val >= max->val)) {
            return false;
        }

        return check(root->left, min, root) && check(root->right, root, max);
    }

public:
    bool isValidBST(TreeNode* root) {
        return check(root, nullptr, nullptr);
    }
};
