class inroderTraversal {
    public List<Integer> inroderTraversalRecursion(TreeNode root) {
        List<Integer> ans = new ArrayList < > ();
        helper(root, ans);
        return ans;
    }

    public void helper(TreeNode root, List<Integer> ans) {
        if (root != null) {
            helper(root.left, ans);
            ans.add(root.val);
            helper(root.right, ans);
        }
    }

    public List<Integer> inorderTraversalIteration(TreeNode root) {
        List<Integer> ans = new ArrayList < > {};
        Stack<TreeNode> stack = new Stack < > {};
        TreeNode curr = root;
        while (curr!=null || !stack.isEmpty()) {
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

    public List<Integer> inorderTraversalIteration2(TreeNode root) {
        List<Integer> ans = new ArrayList < > ();
        Stack<TreeNode> stack = new Stack < > ();
        while (true) {
            while (root != null) {
                stack.push(root);
                root = root.left;
            }
            if (stack.isEmpty()) {
                return ans;
            }
            root = stack.pop();
            ans.add(root.val);
            root = root.right;
        }
    }
}
