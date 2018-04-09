class LinkedList():
    def __init__(self, value=None):
        self.value = value
        # 前驱
        self.before = None
        # 后继
        self.behind = None

    def __str__(self):
        if self.value is not None:
            return str(self.value)
        else:
            return 'None'


def init():
    return LinkedList('HEAD')


def delete(linked_list):
    if isinstance(linked_list, LinkedList):
        if linked_list.behind is not None:
            delete(linked_list.behind)
            linked_list.behind = None
            linked_list.before = None
        linked_list.value = None


def insert(linked_list, index, node):
    node = LinkedList(node)
    if isinstance(linked_list, LinkedList):
        i = 0
        while linked_list.behind is not None:
            if i == index:
                break
            i += 1
            linked_list = linked_list.behind
        if linked_list.behind is not None:
            node.behind = linked_list.behind
            linked_list.behind.before = node
        node.before, linked_list.behind = linked_list, node


def remove(linked_list, index):
    if isinstance(linked_list, LinkedList):
        i = 0
        while linked_list.behind is not None:
            if i == index:
                break
            i += 1
            linked_list = linked_list.behind
        if linked_list.behind is not None:
            linked_list.behind.before = linked_list.before
        if linked_list.before is not None:
            linked_list.before.behind = linked_list.behind
        linked_list.behind = None
        linked_list.before = None
        linked_list.value = None


def trave(linked_list):
    if isinstance(linked_list, LinkedList):
        print(linked_list)
        if linked_list.behind is not None:
            trave(linked_list.behind)


def find(linked_list, index):
    if isinstance(linked_list, LinkedList):
        i = 0
        while linked_list.behind is not None:
            if i == index:
                return linked_list
            i += 1
            linked_list = linked_list.behind
        else:
            if i < index:
                raise Exception(404)
            return linked_list


if __name__ == '__main__':
    linked_list = init()
    trave(linked_list)
    # delete(linked_list)
    insert(linked_list, 0, 1)
    insert(linked_list, 0, 2)
    insert(linked_list, 0, 3)
    remove(linked_list, 2)
    trave(linked_list)
    print(find(linked_list, 3))
