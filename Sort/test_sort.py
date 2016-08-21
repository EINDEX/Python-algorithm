from unittest import TestCase


def get_random_arr(max_num, length, is_int=False):
    """生成随机序列"""
    import random
    if is_int:
        return [int(random.uniform(0, 5000)) for x in range(1000)]
    else:
        return [random.uniform(0, max_num) for x in range(length)]


def create_arr_list():
    """测试序列"""
    arr_list = [[], [0], [1]]
    for x in range(10):
        arr1 = get_random_arr(10 ** x, 10 ** x)
        arr2 = get_random_arr(10 ** x, 10 ** x, True)
        arr_list.append(arr1)
        arr_list.append(arr2)
    return arr_list


def log_sort(func):
    arr_list = create_arr_list()

    def wrapper(*args, **kw):
        import time
        start = time.time()
        for arr in arr_list:
            func(arr=arr, *args, **kw)
        over = time.time()
        print(func.__name__ + ' time: %f' % (over - start))
        return

    return wrapper


class TestSort(TestCase):
    @log_sort
    def test_bubble_sort(self, arr):
        from Sort.bubble_sort import bubble_sort
        if not sorted(arr) == bubble_sort(arr):
            self.fail()

    @log_sort
    def test_bubble_sort_flag(self, arr):
        from Sort.bubble_sort import bubble_sort_flag
        if not sorted(arr) == bubble_sort_flag(arr):
            self.fail()

    @log_sort
    def test_heap_sort(self, arr):
        from Sort.heap_sort import heap_sort
        if not sorted(arr) == heap_sort(arr):
            self.fail()

    @log_sort
    def test_insert_sort(self, arr):
        from Sort.insert_sort import insert_sort
        if not sorted(arr) == insert_sort(arr):
            self.fail()

    @log_sort
    def test_merge_sort(self, arr):
        from Sort.marge_sort import merge_sort
        if not sorted(arr) == merge_sort(arr):
            self.fail()

    @log_sort
    def test_quick_sort(self, arr):
        from Sort.quick_sort import quick_sort
        if not sorted(arr) == quick_sort(arr):
            self.fail()

    @log_sort
    def test_quick_sort_cookbook(self, arr):
        from Sort.quick_sort import quick_sort_cookbook
        if not sorted(arr) == quick_sort_cookbook(arr):
            self.fail()

    @log_sort
    def test_selection_sort(self, arr):
        from Sort.selection_sort import selection_sort
        if not sorted(arr) == selection_sort(arr):
            self.fail()

    @log_sort
    def test_shell_sort(self, arr):
        from Sort.shell_sort import shell_sort
        if not sorted(arr) == shell_sort(arr):
            self.fail()

    @log_sort
    def test_count_sort(self, arr):
        from Sort.count_sort import count_sort
        if len(arr) == 0:
            if not sorted(arr) == count_sort(arr):
                self.fail()
        elif isinstance(arr[0], int):
            if not sorted(arr) == count_sort(arr):
                self.fail()
