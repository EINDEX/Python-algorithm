#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def count_sort(list):
    min = 2147483647
    max = 0
    # 第一步 取得最大值和最小值
    for x in list:
        if x < min:
            min = x
        if x > max:
            max = x
    # 创建数组C
    count = [0] * (max - min +1)
    for index in list:
        count[index - min] += 1
    index = 0
    for a in range(max - min+1):
        for c in range(count[a]):
            list[index] = a + min
            index += 1
    return list
