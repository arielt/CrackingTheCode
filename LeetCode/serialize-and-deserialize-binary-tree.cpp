// https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

#include <sstream>

using namespace std;

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
private:
    void serialize_(TreeNode* node, ostringstream& out) {
        if(node) {
            out << node->val << ' ';
            serialize_(node->left, out);
            serialize_(node->right, out);
        } else {
            out << "# ";
        }
    }

    TreeNode* deserialize_(istringstream& in) {
        string token;
        in >> token;

        if (token == "#") {
            return nullptr;
        }

        TreeNode* node = new TreeNode(stoi(token));
        node->left = deserialize_(in);
        node->right = deserialize_(in);

        return node;
    }

public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        ostringstream out;
        serialize_(root, out);
        return out.str();
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        istringstream in(data);
        return deserialize_(in);
    }
};

// Your Codec object will be instantiated and called as such:
// Codec ser, deser;
// TreeNode* ans = deser.deserialize(ser.serialize(root));