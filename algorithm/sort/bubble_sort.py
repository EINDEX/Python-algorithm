#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""冒泡排序 """


def bubble_sort(arr):
    length = len(arr)
    for index in range(length):
        for j in range(1, length - index):
            if arr[j - 1] > arr[j]:
                # 交换两者数据，这里没用temp是因为python 特性元组。
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
    return arr


def bubble_sort_flag(arr):
    length = len(arr)
    for index in range(length):
        # 标志位
        flag = True
        for j in range(1, length - index):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                flag = False
        if flag:
            # 没有发生交换，直接返回list
            return arr
    return arr
