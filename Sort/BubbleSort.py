#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''冒泡排序 '''


def bubble_sort(list):
    length = len(list)
    for index in range(length):
        for j in range(1, length - index):
            if list[j - 1] > list[j]:
                # 交换两者数据，这里没用temp是因为python 特性元组。
                list[j - 1], list[j] = list[j], list[j - 1]
    return list


def bubble_sort_flag(list):
    length = len(list)
    for index in range(length):
        # 标志位
        flag = True
        for j in range(1, length - index):
            if list[j - 1] > list[j]:
                list[j - 1], list[j] = list[j], list[j - 1]
                flag = False
        if flag:
            # 没有发生交换，直接返回list
            return list
    return list
