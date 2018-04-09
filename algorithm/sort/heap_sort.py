#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def heap_sort(arr):
    # 创建最大堆
    for start in range((len(arr) - 2) // 2, -1, -1):
        sift_down(arr, start, len(arr) - 1)

    # 堆排序
    for end in range(len(arr) - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        sift_down(arr, 0, end - 1)
    return arr


# 最大堆调整
def sift_down(arr, start, end):
    root = start
    while True:
        child = 2 * root + 1
        if child > end:
            break
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1
        if arr[root] < arr[child]:
            arr[root], arr[child] = arr[child], arr[root]
            root = child
        else:
            break
