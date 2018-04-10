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
        elif not self.value:
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
        stack = [self.root]

        while len(stack):
            node = stack.pop()
            if not node.value:
                continue
            for sub_node in node.children[::-1]:
                stack.append(sub_node)
            res.append(node.value)

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

    def preorder_traversal_recursion(self):
        """
        树的前序遍历
        :return: list of tree node value
        """
        res = []
        if not self.root:
            return res

        def _inner(root):
            inner_res = []
            if root.value:
                inner_res.append(root.value)
                for sub_node in root.children:
                    inner_res += _inner(sub_node)
            return inner_res
        return _inner(self.root)

    def postorder_traversal_recursion(self):
        """
        树的后序遍历
        :return: list of tree node value
        """
        res = []
        if not self.root:
            return res

        def _inner(root):
            inner_res = []
            if root.value:
                for sub_node in root.children:
                    inner_res += _inner(sub_node)
                inner_res.append(root.value)
            return inner_res

        return _inner(self.root)

    def layer_while(self):
        """
        树的层序遍历
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

    def layer_recursion(self):
        # todo
        pass

    def depth_recursion(self):

        def _inner(root, depth=1):
            if not root.children:
                return depth
            return max([_inner(sub_node, depth+1) for sub_node in root.children])

        return _inner(self.root)

    def node_count(self):
        def _inner(root):
            if not root.children:
                return 1
            return 1 + sum([_inner(sub_node) for sub_node in root.children])
        return _inner(self.root)

    def leaf_count(self):
        def _inner(root):
            if not root.children:
                return 1
            return sum([_inner(sub_node) for sub_node in root.children])
        return _inner(self.root)

    def lowest_ancestor_node(self, node1, node2):
        stack = [self.root]
        stack1 = None
        stack2 = None

        while len(stack) and not (stack1 and stack2):
            node = stack.pop()

            if node is node1:
                stack1 = stack[:]
            if node is node2:
                stack2 = stack[:]
            if not node.value:
                continue
            for sub_node in node.children:
                stack.append(sub_node)

        res = self.root
        for i in range(len(stack1)):
            if stack1[i] == stack2[i]:
                res = stack1[i]
            else:
                return res.value

        return res.value

    def two_node_distence(self, node1, node2):
        stack = [self.root]
        stack1 = None
        stack2 = None

        while len(stack) and not (stack1 and stack2):
            node = stack.pop()

            if node is node1:
                stack1 = stack[:]
            if node is node2:
                stack2 = stack[:]
            if not node.value:
                continue
            for sub_node in node.children:
                stack.append(sub_node)

        res = self.root
        for i in range(len(stack1)):
            if stack1[i] == stack2[i]:
                res = stack1[i]
            else:
                return len(stack1) + len(stack2) - 2*i

        return len(stack1) + len(stack2) - 2*i


if __name__ == '__main__':
    node1, node2 = TreeNode(6), TreeNode(8)
    t = Tree(
        TreeNode(1, [TreeNode(2, [TreeNode(4), TreeNode(5), node1]), TreeNode(3, [TreeNode(7), node2])]))
    print(t.preorder_traversal_while())
    print(t.postorder_traversal_while())
    print(t.preorder_traversal_recursion())
    print(t.postorder_traversal_recursion())
    print(t.layer_while())
    print(t.depth_recursion())
    print(t.node_count())
    print(t.leaf_count())
    print(t.lowest_ancestor_node(node1, node2))
    print(t.two_node_distence(node1, node2))
