/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public void flatten(TreeNode root) {
        if(root == null) return;
        
        LinkedList<TreeNode> q = new LinkedList<TreeNode>();
        TreeNode c = new TreeNode(-1);
        TreeNode h = c;
        q.add(root);
        
        while (!q.isEmpty()) {
            c.right = q.pop(); // get first
            c = c.right;
            
            if (c.right != null) {
                q.push(c.right);
                c.right = null;
            }

            if (c.left != null) {
                q.push(c.left);
                c.left = null;
            }            
        }
        
        h.right = null; // null it to allow garbage collection
    }
}

