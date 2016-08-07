#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''测试函数 '''
import random
import time

from Sort.BubbleSort import bubble_sort, bubble_sort_flag
from Sort.CountSort import count_sort
from Sort.HeapSort import heap_sort
from Sort.InsertSort import insert_sort
from Sort.MargeSort import merge_sort
from Sort.QuickSort import quick_sort, qsort
from Sort.SelectionSort import selection_sort
from Sort.ShellSort import shell_sort
import sys

# 开挂 防止栈溢出
sys.setrecursionlimit(99999)

#整数数列
# L = [int(random.uniform(0, 5000)) for x in range(1000)]
# 浮点数列
L = [random.uniform(0, 5000) for x in range(1000)]

current = list(L)
current.sort()

def compile(fun):
    l = list(L)
    start=time.time()
    res = fun(l)
    over = time.time()
    print('time:'+str(over-start),current == res, fun.__name__)


compile(selection_sort)
compile(bubble_sort)
compile(bubble_sort_flag)
compile(insert_sort)
compile(merge_sort)
compile(shell_sort)
compile(quick_sort)
compile(qsort)
compile(heap_sort)
if isinstance(L[0],int):
    compile(count_sort)
