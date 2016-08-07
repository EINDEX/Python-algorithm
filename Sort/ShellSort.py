#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def shell_sort(list):
    n = len(list)
    # 初始步长
    gap = round(n / 2)
    while gap > 0:
        for i in range(gap, n):
            # 每个步长进行插入排序
            temp = list[i]
            j = i
            # 插入排序
            while j >= gap and list[j - gap] > temp:
                list[j] = list[j - gap]
                j -= gap
            list[j] = temp
        # 得到新的步长
        gap = round(gap / 2)
    return list