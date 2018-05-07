#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def shell_sort(arr):
    n = len(arr)
    # 初始步长
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            # 每个步长进行插入排序
            temp = arr[i]
            j = i
            # 插入排序
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        # 得到新的步长
        gap = gap // 2
    return arr
