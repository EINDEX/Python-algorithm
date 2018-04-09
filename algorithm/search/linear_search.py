def linear_search(arr, key):
    """顺序(线性)查找算法实现"""
    for value in arr:
        # 寻找目标
        while value == key:
            return value