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
        List <Integer> ans = new ArrayList < > ();
        Stack <TreeNode> stack = new Stack < > ();
        TreeNode curr = root;
        while (curr != null || !stack.isEmpty()) {
            while (curr != null) {
                stack.push(curr);
                curr = curr.left;
            }
            curr = stack.pop();
            ans.add(curr.val);
            curr = curr.right;
        }
        return ans;
    }
 }
