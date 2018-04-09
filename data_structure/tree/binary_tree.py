from data_structure.tree.tree import Tree, TreeNode


class BinaryTreeNode(TreeNode):
    """
    一个二叉树节点
    """

    def __init__(self, value, left, right):
        self.left = left
        self.right = right
        super().__init__(value, [left, right])


class BinaryTree(Tree):
    """
    二叉树：基本二叉树的数据结构
    """

    def inorder_traversal_while(self):
        """
        二叉树的中序遍历
        :return: list of node values
        """
        res = []

        if not self.root:
            return res

        stack = [self.root]
        node = self.root.left

        while len(stack):
            while node:
                stack.append(node)
                node = node.left

            res.append(stack[-1].value)

        return res
