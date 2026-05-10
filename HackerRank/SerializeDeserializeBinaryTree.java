// BFS solution

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        StringBuilder rv = new StringBuilder();
        
        if (root == null) return "";
        
        LinkedList<TreeNode> queue = new LinkedList<TreeNode>();
        queue.add(root);
        boolean first = true;
        while (!queue.isEmpty()) {
            TreeNode node = queue.remove();
            if (!first) {
                rv.append(":");
            }
            if (node == null) {
                rv.append("N");
            } else {
                rv.append(node.val);
                queue.add(node.left);
                queue.add(node.right);
            }
            first = false;
        }
        return rv.toString();
    }
    
    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if (data == null) return null;
        if (data == "") return null;

        String[] nodes = data.split(":");
        if (nodes.length == 0) return null;
        
        LinkedList<TreeNode> queue = new LinkedList<TreeNode>();
        TreeNode root = new TreeNode(Integer.parseInt(nodes[0]));
        queue.add(root);
        for (int i=1; i<nodes.length; i += 2) {
            TreeNode parent = queue.poll();
            if (nodes[i].equals("N")) {
                parent.left = null;
            } else {
                parent.left = new TreeNode(Integer.parseInt(nodes[i]));
                queue.add(parent.left);
            }
            
            if (nodes[i+1].equals("N")) {
                parent.right = null;
            } else {
                parent.right = new TreeNode(Integer.parseInt(nodes[i+1]));
                queue.add(parent.right);
            }
        }
        return root;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));

