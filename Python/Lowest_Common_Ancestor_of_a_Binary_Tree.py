class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None

        def findsub(node):
            nonlocal ans
            if not node:
                return False
            cres = node == p or node == q
            lres = findsub(node.left)
            rres = findsub(node.right)
            if sum([cres, lres, rres]) >= 2:
                ans = node
            return cres or lres or rres

        findsub(root)
        return ans
