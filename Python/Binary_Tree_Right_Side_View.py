from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []

        def findRight(node, level):
            if node:
                if len(res) == level:
                    res.append(None)
                res[level] = node.val
                findRight(node.left, level + 1)
                findRight(node.right, level + 1)

        findRight(root, 0)
        return res
