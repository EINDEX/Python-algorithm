class MyStack(object):
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


def top(stack):
    if isinstance(stack, MyStack):
        if stack.behind is not None:
            return top(stack.behind)
        else:
            return stack


def push(stack, ele):
    push_ele = MyStack(ele)
    if isinstance(stack, MyStack):
        stack_top = top(stack)
        push_ele.before = stack_top
        push_ele.before.behind = push_ele


def pop(stack):
    if isinstance(stack, MyStack):
        stack_top = top(stack)
        if stack_top.before is not None:
            stack_top.before.behind = None
            stack_top.behind = None
            return stack_top
        else:
            print('已经是栈顶了')
