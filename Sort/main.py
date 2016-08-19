#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试函数 """
import random
import time

from Sort.bubble_sort import bubble_sort, bubble_sort_flag
from Sort.count_sort import count_sort
from Sort.heap_sort import heap_sort
from Sort.insert_sort import insert_sort
from Sort.marge_sort import merge_sort
from Sort.quick_sort import quick_sort, qsort
from Sort.selection_sort import selection_sort
from Sort.shell_sort import shell_sort
import sys

# 开挂 防止栈溢出
sys.setrecursionlimit(99999)

# 整数数列
# L = [int(random.uniform(0, 5000)) for x in range(1000)]
# 浮点数列
L = [random.uniform(0, 5000) for x in range(1000)]
current = list(L)
current.sort()


def sort_test(fun):
    l = list(L)
    start = time.time()
    res = fun(l)
    over = time.time()
    print('time:' + str(over - start), current == res, fun.__name__)


sort_test(selection_sort)
sort_test(bubble_sort)
sort_test(bubble_sort_flag)
sort_test(insert_sort)
sort_test(merge_sort)
sort_test(shell_sort)
sort_test(quick_sort)
sort_test(qsort)
sort_test(heap_sort)
if isinstance(L[0], int):
    sort_test(count_sort)
