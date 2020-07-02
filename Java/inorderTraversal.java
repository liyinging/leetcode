class inorderTraversal {
    public List<Integer> inorderTraversalRecursion(TreeNode root) {
        List<Integer> ans = new ArrayList < > ();
        traverse(root, ans);
        return ans;
    }

    public void traverse(TreeNode node, List <Integer> ans) {
        if (node != null) {
            traverse(node.left, ans);
            ans.add(node.val);
            traverse(node.right, ans);
        }
    }

    public List<Integer> inorderTraversalIteration(TreeNode root) {

    }
 }
