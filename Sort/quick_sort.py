#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def quick_sort(arr):
    less = []
    pivot_list = []
    more = []
    # 递归出口
    if len(arr) <= 1:
        return arr
    else:
        # 将第一个值做为基准
        pivot = arr[0]
        for i in arr:
            # 将比急转小的值放到less数列
            if i < pivot:
                less.append(i)
            # 将比基准打的值放到more数列
            elif i > pivot:
                more.append(i)
            # 将和基准相同的值保存在基准数列
            else:
                pivot_list.append(i)
        # 对less数列和more数列继续进行排序
        less = quick_sort(less)
        more = quick_sort(more)
        return less + pivot_list + more


def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        return qsort([x for x in arr[1:] if x < pivot]) + \
               [pivot] + \
               qsort([x for x in arr[1:] if x >= pivot])
