// https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/

#include <algorithm>

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
    int maxDepth(TreeNode* root) {
        if (!root) {
            return 0;
        }

        // int left = maxDepth(root->left);
        // int right = maxDepth(root->right);

        return max(maxDepth(root->left), maxDepth(root->right)) + 1;
    }
};
