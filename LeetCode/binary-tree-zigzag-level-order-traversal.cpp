#include <deque>
#include <queue>

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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> rv = {};
        if (!root) {
            return rv;
        }

        queue<TreeNode*> q;
        bool dir = true;

        q.push(root);

        while (!q.empty()) {
            // empty the current level
            int s = q.size();
            deque<int> level;
            while (s) {
                TreeNode* node = q.front();
                q.pop();

                if (node->left) {
                    q.push(node->left);
                }

                if (node->right) {
                    q.push(node->right);
                }

                if(dir) {
                    level.push_back(node->val);
                } else {
                    level.push_front(node->val);
                }
                s--;
            }

            dir = !dir;
            rv.push_back(vector<int>(level.begin(), level.end()));
        }

        return rv;        
    }
};
