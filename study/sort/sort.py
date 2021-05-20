def bubble_sort(arr):
    """
    冒泡排序

    比较相邻的元素。如果第一个比第二个大，就交换他们两个。

    对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。

    针对所有的元素重复以上的步骤，除了最后一个。

    持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
    :param arr:
    :return:
    """
    for n in range(len(arr)-1):
        for m in range(len(arr) - 1 - n):
            if arr[m] > arr[m+1]:
                arr[m], arr[m+1] = arr[m+1], arr[m]
    return arr


def selection_sort(arr):
    """
    选择排序
    首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置

    再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。

    重复第二步，直到所有元素均排序完毕。
    :param arr:
    :return:
    """
    for i in range(len(arr) - 1):
        minindex = i
        for j in range(i, len(arr)):
            if arr[j] < arr[minindex]:
                minindex = j
        if minindex != i:
            arr[i], arr[minindex] = arr[minindex], arr[i]
    return arr


def insertion_sort(arr):
    for i in range(len(arr)):
        preindex = i-1
        current = arr[i]
        while preindex >= 0 and arr[preindex] > current:
            arr[preindex+1] = arr[preindex]
            preindex -= 1
        arr[preindex+1] = current
    return arr


def insert_sort(arr):
    """
    插入排序
    将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。

    从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。
    （如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）
    :param arr:
    :return:
    """
    for i in range(len(arr) - 1):
        c = arr[i]
        while i > 0 and c < arr[i-1]:
            arr[i] = arr[i-1]
            i -= 1
        arr[i] = c
    return arr


def quick_sort(arr):
    if len(arr) >= 2:
        m = arr[0]
        left, right = [], []
        arr.remove(m)
        for i in arr:
            if i >= m:
                right.append(i)
            else:
                left.append(i)
        return quick_sort(left) + [m] + quick_sort(right)
    else:
        return arr


def bucket_sort(arr):
    dp = [[] for _ in range(10)]
    for i in arr:
        cur = i % 10
        dp[cur].append(i)
    arr.clear()
    for k, v in enumerate(dp):
        for m in v:
            arr.append(m)
        dp[k].clear()
    for j in arr:
        cur1 = int(j / 10)
        dp[cur1].append(j)
    arr.clear()
    for v in dp:
        for m in v:
            arr.append(m)
    print(dp)
    return arr


arr = [15, 6, 3, 7, 8, 67]
# print(bubble_sort(arr))
# print(selection_sort(arr))
# print(insert_sort(arr))
# print(quick_sort(arr))
print(bucket_sort(arr))
