from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        def helper(node, level):
            nonlocal ans
            if node:
                if level == len(ans):
                    ans.append([])
                ans[level].append(node.val)
                helper(node.left, level + 1)
                helper(node.right, level + 1)
        helper(root, 0)
        return ans
