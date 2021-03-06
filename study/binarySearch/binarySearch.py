# 二分搜索是一种在有序数组中查找某一特定元素的搜索算法。
# 搜索过程从数组的中间元素开始，如果中间元素正好是要查找的元素，则搜索过程结束；
# 如果某一特定元素大于或者小于中间元素，则在数组大于或小于中间元素的那一半中查找，
# 而且跟开始一样从中间元素开始比较。如果在某一步骤数组为空，则代表找不到。
# 这种搜索算法每一次比较都使搜索范围缩小一半。


def binarysearch(arr, ret, l, r):
    lenth = len(arr[l:r])
    mid = int(l + lenth / 2)
    if lenth:
        if arr[mid] == ret:
            return mid
        elif arr[mid] < ret:
            return binarysearch(arr, ret, mid, lenth)
        else:
            return binarysearch(arr, ret, 0, mid)
    else:
        return -1


arr = []
ret = 10
print(binarysearch(arr, ret, 0, len(arr)))
