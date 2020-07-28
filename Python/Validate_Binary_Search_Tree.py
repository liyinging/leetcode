class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node):
            if not node:
                return float('inf'), float('-inf'), True
            lmin, lmax, lres = helper(node.left)
            rmin, rmax, rres = helper(node.right)
            return min(node.val, lmin, rmin), max(node.val, lmax, rmax), lmax < node.val < rmin and lres and rres
        _, _, res = helper(root)
        return res
