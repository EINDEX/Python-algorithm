#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def selection_sort(arr):
    n = len(arr)
    # 遍历所有元素
    for i in range(0, n):
        # 获取最小元素的
        min_num = i
        # 遍历未排序元素
        for j in range(i + 1, n):
            # 找到一个比最小元素小的元素
            if arr[j] < arr[min_num]:
                min_num = j
                # 交换数据
        arr[min_num], arr[i] = arr[i], arr[min_num]
    return arr
