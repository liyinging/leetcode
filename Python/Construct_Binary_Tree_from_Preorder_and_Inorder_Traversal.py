from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(preorder, left, right):
            nonlocal maps
            if left > right:
                return None
            val = preorder.pop(0)
            idx = maps[val]
            root = TreeNode(val)
            root.left = build(preorder, left, idx - 1)
            root.right = build(preorder, idx + 1, right)
            return root
        maps = {val: idx for idx, val in enumerate(inorder)}
        root = build(preorder, 0, len(inorder) - 1)
        return root
