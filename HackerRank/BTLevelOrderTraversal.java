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
    public List<List<Integer>> levelOrder(TreeNode root) {        
        List rv = new ArrayList<List<Integer>>();
        if (root == null) return rv;

        int l = 0;
        LinkedList<TreeNode> q = new LinkedList<TreeNode>();
        q.add(root);
        
        while(!q.isEmpty()) {
            int levelSize = q.size();
            ArrayList<Integer> level = new ArrayList<Integer>();
            
            for (int i=0; i<levelSize; i++) {
                TreeNode n = q.poll();
                level.add(n.val);
                if (n.left != null) q.add(n.left);
                if (n.right != null) q.add(n.right);
            }
            rv.add(level);
        }
        
        return rv;
    }
}
