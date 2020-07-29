class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def findmax(node):
            nonlocal ans
            if not node:
                return 0
            lmax = max(findmax(node.left), 0)
            rmax = max(findmax(node.right), 0)
            cmax = lmax + node.val + rmax
            ans = max(ans, cmax)
            return max(lmax, rmax) + node.val
        ans = float('-inf')
        findmax(root)
        return ans
