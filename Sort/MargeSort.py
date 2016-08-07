#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def merge_sort(list):
    # 认为长度不大于1的数列是有序的
    if len(list) <= 1:
        return list
    # 二分列表
    middle = len(list) // 2
    left = merge_sort(list[:middle])
    right = merge_sort(list[middle:])
    # 最后一次合并
    return merge(left, right)


# 合并
def merge(left, right):
    l, r = 0, 0
    result = []
    # 两个子数列比大小
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    # 填充结果
    result += left[l:]
    result += right[r:]
    return result
