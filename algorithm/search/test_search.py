from unittest import TestCase


def get_random_arr(max_num, length):
    import random
    return [random.uniform(0, max_num) for x in range(length)]


def create_arr_list():
    """测试序列"""
    arr_list = [[0], [0, 1]]
    for x in range(6):
        arr = get_random_arr(10 ** x, 10 ** x)
        arr_list.append(arr)
    return arr_list


def search_log(func):
    import time, random
    arr_list = create_arr_list()

    def wrapper(*args, **kw):
        start = time.time()
        for arr in arr_list:
            key = random.choice(arr)
            func(arr=arr, key=key, *args, **kw)
        over = time.time()
        print(func.__name__ + ' time: %f' % (over - start))
        return

    return wrapper


class TestSearch(TestCase):
    @search_log
    def test_linear_search(self, arr, key):
        from search.linear_search import linear_search
        if not key == linear_search(arr, key):
            self.fail()

    @search_log
    def test_binary_search_while(self, arr, key):
        from search.binary_search import binary_search_while
        if not key == binary_search_while(arr, key):
            self.fail()

    @search_log
    def test_binary_search_re(self, arr, key):
        from search.binary_search import binary_search_re
        if not key == binary_search_re(arr, key):
            self.fail()
