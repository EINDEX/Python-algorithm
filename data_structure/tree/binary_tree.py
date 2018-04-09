from data_structure.tree.Tree import Tree


class BinaryTree(Tree):
    """
    二叉树：基本二叉树的数据结构
    """
    def __init__(self, key):
        self.key = key
        self._r_child = None
        self._l_child = None
        super().__init__(key=key, children=[self._l_child, self._r_child])

    @property
    def l_child(self):
        return self._l_child

    @l_child.setter
    def l_child(self, l_child):
        if not isinstance(l_child, BinaryTree): return
        self._l_child = l_child
        self.children = [self.l_child, self.r_child]

    @property
    def r_child(self):
        return self._r_child

    @r_child.setter
    def r_child(self, r_child):
        if not isinstance(r_child, BinaryTree): return
        self._r_child = r_child
        self.children = [self.l_child, self.r_child]
