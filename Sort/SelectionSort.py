#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def selection_sort(list):
    n = len(list)
    # 遍历所有元素
    for i in range(0, n):
        # 获取最小元素的
        min = i
        # 遍历未排序元素
        for j in range(i + 1, n):
            # 找到一个比最小元素小的元素
            if list[j] < list[min]:
                min = j
                # 交换数据
        list[min], list[i] = list[i], list[min]
    return list
