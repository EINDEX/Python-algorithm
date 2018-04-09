import copy

from DataStructure.tree.BinaryTree import BinaryTree


# 二叉查找树
class BST(BinaryTree):
    root = None

    def __init__(self, key, data):
        """
        初始化树
        :param data: 节点值
        """
        self.key = key
        self.data = data
        super().__init__(key)

    def __str__(self):
        return str({
            'key': str(self.key),
            'data': str(self.data)
        })



    # 再书中找到一个值
    def get(self, key):
        """

        :param key: 需要找到的值
        :return: 节点
        """

        def inner_func(node, _key):
            """

            :param node: 节点
            :param _key: 值
            :return: 找到值时返回节点，未找到时,递归或者返回None
            """
            if node is None:
                return None
            if _key > node.key:
                return inner_func(node.r_child, _key)
            elif _key < node.key:
                return inner_func(node.l_child, _key)
            else:
                return node

        return inner_func(self.root, key)

    def put(self, key, value):
        """
        如果 key存在就更新 value，如果 key 不存在就插入新节点
        如果根节点不存在就创建一个 BST 实例
        :param key:
        :param value:
        :return:
        """
        if self.root is None:
            return BST(key, value)

        def inner_func(node, _key, _value):
            if node is None:
                return BST(_key, _value)
            if _key > node.key:
                node.r_child = inner_func(node.r_child, _key, _value)
            elif _key < node.key:
                node.l_child = inner_func(node.l_child, _key, _value)
            else:
                node.data = _value
            return node

        return inner_func(self.root, key, value)

    def select(self, num):
        """
        选出第num小的元素
        :param num:
        :return: 节点
        """

        def inner_select(node, _num):
            if node is None:
                return
            t = node.l_child.size()
            if _num < t:
                return inner_select(node.l_child, _num)
            elif _num > t:
                return inner_select(node.r_child, _num - t - 1)
            else:
                return node

        return inner_select(self.root, num)

    def min(self):
        def inner_min(node):
            if node.l_child is None:
                return node
            else:
                return inner_min(node.l_child)

        return inner_min(self)

    def rank(self, key):
        """
        获得给定键的排名
        :param key:
        :return:
        """

        def inner_rank(node, _key):
            if node is None:
                return
            if _key > node.key:
                return inner_rank(node.r_child, _key)
            elif _key < node.key:
                return 1 + node.l_child.size() + inner_rank(node.l_child, _key)
            else:
                if node.l_child is None:
                    return 0
                else:
                    return node.l_child.size()

        return inner_rank(self.root, key)

    def delete(self, key):
        """
        删除指定 key 的键
        :param key:
        :return:
        """

        def delete_min_node(node):
            if node.l_child is None:
                return node.r_child
            node.l_child = delete_min_node(node.l_child)
            return node

        def inner_delete(node, _key):
            if node is None:
                return
            if _key > node.key:
                node.r_child = inner_delete(node.r_child, _key)
            elif _key < node.key:
                node.l_child = inner_delete(node.l_child, _key)
            else:
                if node.r_child is None:
                    return node.l_child
                elif node.l_child is None:
                    return node.r_child
                temp = copy.copy(node)
                node = min(temp.right)
                node.r_child = delete_min_node(temp.r_child)
                node.l_child = temp.l_chlid
            return node

        return delete_min_node(self)

    def find_keys(self, low, high):
        """
        查找范围内所有的数
        :param low:
        :param high:
        :return:
        """
        BST_list = []

        def inner_find_keys(node, _low, _high):
            if node is None:
                return
            if _low < node.key:
                inner_find_keys(node.l_child, _low, _high)
            if _low <= node.key <= _high:
                BST_list.append(node)
            if _high > node.key:
                inner_find_keys(node.r_child, _low, _high)

        inner_find_keys(self, low, high)
        return BST_list


if __name__ == '__main__':
    root = BST(50, "2")
    root.put(3, "5")
    root.put(5, "5")
    root.put(80, "5")
    root.put(60, "5")
    root.print_tree()
    print(root.get(60))
    print(root.select(2))
    print(root.rank(5))
    root.delete(5)
    print(root.min())
    root.print_tree()
    for node in root.find_keys(50, 100):
        print(node)
