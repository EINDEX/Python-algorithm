class MyQueue():
    def __init__(self, value=None):
        self.value = value
        # 前驱
        # self.before = None
        # 后继
        self.behind = None

    def __str__(self):
        if self.value is not None:
            return str(self.value)
        else:
            return 'None'


def create_queue():
    """仅有队头"""
    return MyQueue()


def last(queue):
    if isinstance(queue, MyQueue):
        if queue.behind is not None:
            return last(queue.behind)
        else:
            return queue


def push(queue, ele):
    if isinstance(queue, MyQueue):
        last_queue = last(queue)
        new_queue = MyQueue(ele)
        last_queue.behind = new_queue


def pop(queue):
    if queue.behind is not None:
        get_queue = queue.behind
        queue.behind = queue.behind.behind
        return get_queue
    else:
        print('队列里已经没有元素了')


def print_queue(queue):
    print(queue)
    if queue.behind is not None:
        print_queue(queue.behind)


if __name__ == '__main__':
    queue = create_queue()
    push(queue, 1)
    push(queue, 2)
    push(queue, 3)
    push(queue, 4)
    print_queue(queue)
    print(pop(queue))
    print(pop(queue))
    print(pop(queue))
    print(pop(queue))
    print(pop(queue))
