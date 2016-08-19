def linear_search(arr, key):
    """顺序(线性)查找算法实现"""
    for index, value in enumerate(arr):
        # 寻找目标
        if value == key:
            return index
