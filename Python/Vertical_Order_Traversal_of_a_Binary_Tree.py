from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        ans = []
        stack = [(0, 0, root)]
        while stack:
            c, r, node = stack.pop()
            if node:
                ans.append((c, r, node.val))
                stack.append((c + 1, r + 1, node.right))
                stack.append((c - 1, r + 1, node.left))
        ans.sort()
        res = defaultdict(list)
        for c, r, v in ans:
            res[c].append(v)
        return res.values()
