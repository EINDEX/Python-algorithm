class Tree(object):
    height = None
    weight = None
    root = None

    def __init__(self, key, children):
        self.children = children
        self.key = key
        if self.root is None:
            self.root = self

    def depth(self):
        if self.root is None:
            return 0

        def depth_func(node):
            if len(node.children) == 0:
                return 1
            depth_child = []
            for child in node.children:
                depth_child.append(depth_func(child) + 1)
            return max(depth_child)

        return depth_func(self.root)

    def print_tree(self):
        if self.root is None:
            print('tree is None')
            return

        def print_func(node, depth):
            if node is None:
                return
            if depth == 0:
                print('   ' * depth + str(node.key))
            else:
                print(' ' + '   ' * (depth - 1) + '--' + str(node.key))
            for child in node.children:
                print_func(child, depth + 1)

        print_func(self.root, 0)

    def size(self):
        def inner_size(node):
            """
            子树的大小
            :param node:
            :return:
            """
            size_num = 0
            if node is None:
                return size_num
            for child in node.children:
                size_num += inner_size(child)
            return size_num + 1

        return inner_size(self)

if __name__ == '__main__':
    root = Tree(1, [Tree(2, [Tree(3, [])]), Tree(4, [])])
    print(root.depth())
    root.print_tree()
    print(root.children[0].size())
