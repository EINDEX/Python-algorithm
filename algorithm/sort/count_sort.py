#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def count_sort(arr):
    min_num = 2147483647
    max_num = 0
    # 第一步 取得最大值和最小值
    for x in arr:
        if x < min_num:
            min_num = x
        if x > max_num:
            max_num = x
    # 创建数组C
    count = [0] * (max_num - min_num +1)
    for index in arr:
        count[index - min_num] += 1
    index = 0
    for a in range(max_num - min_num+1):
        for c in range(count[a]):
            arr[index] = a + min_num
            index += 1
    return arr
