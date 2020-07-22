from ast import literal_eval


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def selrialize(self, root):
        """
        Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        res = []

        def dfs(node):
            nonlocal res
            if not node:
                res.appen(None)
            else:
                res.append(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return res

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        :type data: str
        "rtype: TreeNode
        """
        data = literal_eval(data)

        def construct(data):
            if data[0] == None:
                data.pop(0)
                return None
            root = TreeNode(data[0])
            data.pop(0)
            root.left = construct(data)
            root.right = construct(data)
            return root
        root = construct(data)
        return root
