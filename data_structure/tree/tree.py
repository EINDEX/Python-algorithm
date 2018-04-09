from queue import Queue


class TreeNode(object):
    """
    一个树节点
    """

    def __init__(self, value, children: list = None):
        """

        :param value: 节点的值
        :param children: 节点的子节点，一个 TreeNode 的列表
        """

        self.value = value

        if not children:
            self.children = []
        else:
            self.children = children


class Tree(object):
    """
    树：基本树的数据结构
    """

    def __init__(self, root: TreeNode or None):
        """
        传入根节点
        :param root: 如果为 TreeNode 为根节点， 如果为 None 为空书
        """
        if not (root is None or isinstance(root, TreeNode)):
            raise AttributeError('illegal root')
        self.root = root

    def preorder_traversal_while(self):
        """
        树的前序遍历
        :return: list of tree node value
        """
        res = []
        if not self.root:
            return res

        queue = Queue()
        queue.put(self.root)

        while queue.qsize():
            node = queue.get()
            if not node.value:
                continue
            res.append(node.value)
            for sub_node in node.children:
                queue.put(sub_node)
        return res

    def postorder_traversal_while(self):
        """
        树的后序遍历
        :return: list of tree node value
        """
        res = []

        if not self.root:
            return res

        stack = [self.root]

        while len(stack):
            node = stack.pop()
            if not node.value:
                continue
            for sub_node in node.children:
                stack.append(sub_node)
            res.append(node.value)

        return res[::-1]


if __name__ == '__main__':
    t = Tree(
        TreeNode(1, [TreeNode(2, [TreeNode(4), TreeNode(5), TreeNode(6)]), TreeNode(3, [TreeNode(7), TreeNode(8)])]))
    print(t.preorder_traversal_while())
    print(t.postorder_traversal_while())
