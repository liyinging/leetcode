from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversalRecursion(self, root: TreeNode) -> List[int]:
        ans = []

        def traverse(node):
            nonlocal ans
            if node:
                traverse(node.left)
                ans.append(node.val)
                traverse(node.right)

        traverse(root)
        return ans

    def inorderTraversalIteration(self, root: TreeNode) -> List[int]:
        stack, ans = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return ans
            node = stack.pop()
            ans.append(node.val)
            root = node.right
