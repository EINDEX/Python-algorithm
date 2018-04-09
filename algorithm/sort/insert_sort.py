#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def insert_sort(arr):
    n = len(arr)
    for i in range(1, n):
        # 后一个元素和前一个元素比较
        # 如果比前一个小
        if arr[i] < arr[i - 1]:
            # 将这个数取出
            temp = arr[i]
            # 保存下标
            index = i
            # 从后往前依次比较每个元素
            for j in range(i - 1, -1, -1):
                # 和比取出元素大的元素交换
                if arr[j] > temp:
                    arr[j + 1] = arr[j]
                    index = j
                else:
                    break
            # 插入元素
            arr[index] = temp
    return arr
