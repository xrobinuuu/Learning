import copy
import random
import threading
import time


class SleepTime:
    def sleep_time(self, ls, num, scale):
        time.sleep(num / scale)
        ls.append(num)

    def sleep_sort(self, res):
        ls = list()
        td_ls = list()
        for n in res:
            td = threading.Thread(target=self.sleep_time, args=(ls, n, 10))
            td.start()
            td_ls.append(td)
        for tmp in td_ls:
            tmp.join()
        return ls


def quicksort(arr):
    if len(arr) < 2:
        return arr
    left = list()
    right = list()
    position_arg = arr.pop()
    # position_arg = li.pop(random.randint(0, lenth - 1))
    for num in arr:
        if num < position_arg:
            left.append(num)
        else:
            right.append(num)

    return quicksort(left) + [position_arg] + quicksort(right)


def bubblesort(arr):
    print("-------------->", arr)
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def selectsort(arr):
    print("-------------->", arr)

    for i in range(len(arr) - 1):
        mini = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[mini]:
                mini = j
            if i != mini:
                arr[i], arr[mini] = arr[mini], arr[i]
    return arr


def insertsort(arr):
    print("-------------->", arr)

    for i in range(len(arr)):
        leftindex = i - 1
        current = arr[i]
        while leftindex >= 0 and arr[leftindex] > current:
            arr[leftindex + 1] = arr[leftindex]
            arr[leftindex] = current
            leftindex -= 1
    return arr


def shellsort(arr):
    import math
    gap = 1
    while gap < (len(arr) / 3):
        gap = gap * 3 + 1
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i - gap
            while j >= 0 and arr[j] > temp:
                arr[j + gap] = arr[j]
                j -= gap
            arr[j + gap] = temp
        gap = math.floor(gap / 3)
        # gap = divmod(gap, 3)[0]
    return arr


class MergeSort:
    def mergesort(self, arr):
        import math
        if len(arr) < 2:
            return arr
        middle = math.floor(len(arr) / 2)
        left, right = arr[0:middle], arr[middle:]
        return self.merge(self.mergesort(left), self.mergesort(right))

    def merge(self, left, right):
        result = []
        while left and right:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        while left:
            result.append(left.pop(0))
        while right:
            result.append(right.pop(0))
        return result


class HeapSort:
    def buildMaxHeap(self, arr):
        import math
        for i in range(math.floor(len(arr) / 2), -1, -1):
            self.heapify(arr, i)

    def heapify(self, arr, i):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        if left < arrLen and arr[left] > arr[largest]:
            largest = left
        if right < arrLen and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            self.swap(arr, i, largest)
            self.heapify(arr, largest)

    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def heapSort(self, arr):
        global arrLen
        arrLen = len(arr)
        self.buildMaxHeap(arr)
        for i in range(len(arr) - 1, 0, -1):
            self.swap(arr, 0, i)
            arrLen -= 1
            self.heapify(arr, 0)
        return arr


def bucketSort(nums):
    max_num = max(nums)
    bucket = [0] * (max_num + 1)
    for i in nums:
        bucket[i] += 1
    sort_nums = []
    for j in range(len(bucket)):
        if bucket[j] != 0:
            for y in range(bucket[j]):
                sort_nums.append(j)
    return sort_nums


if __name__ == "__main__":
    dic = dict()
    tes = [random.randint(-11000, 20000) for i in range(10000)]
    for i in range(20):
        test = "tes" + str(i)
        dic.update({test: copy.deepcopy(tes)})

    print("tes:", copy.deepcopy(tes))
    t_1 = time.perf_counter()
    res1 = sorted(tes)
    t_2 = time.perf_counter()
    print("--------->sort:", res1, "--->time:", t_2 - t_1)

    st = SleepTime()
    # res2 = st.sleep_sort(dic['tes1'])
    t_3 = time.perf_counter()
    # print("---->SleepTime:", res2, "--->time:", t_3 - t_2)

    res3 = quicksort(dic['tes2'])
    t_4 = time.perf_counter()
    print("---->QuickSort:", res3, "--->time:", t_4 - t_3)

    # res4 = bubblesort(dic['tes3'])
    t_5 = time.perf_counter()
    # print("--->bubblesort:", res4, "--->time:", t_5 - t_4)

    # res5 = selectsort(dic['tes4'])
    t_6 = time.perf_counter()
    # print("--->selectsort:", res5, "--->time:", t_6 - t_5)

    # res6 = insertsort(dic['tes5'])
    t_7 = time.perf_counter()
    # print("--->insertsort:", res6, "--->time:", t_7 - t_6)

    res7 = shellsort(dic['tes6'])
    t_8 = time.perf_counter()
    print("--->time:", t_8 - t_7, "---->shellsort:", res7)

    ms = MergeSort()
    res8 = ms.mergesort(dic['tes7'])
    t_9 = time.perf_counter()
    print("---->mergesort:", res8, "--->time:", t_9 - t_8)

    hs = HeapSort()
    res9 = hs.heapSort(dic['tes8'])
    t_10 = time.perf_counter()
    print("---->buildMaxHeap:", res9, "--->time:", t_10 - t_9)

    res10 = bucketSort(dic['tes9'])
    t_11 = time.perf_counter()
    print("---->bucktetSort:", res10, "--->time:", t_11 - t_10)

    # res10 = bucketSort([-1, -1])
    # t_11 = time.perf_counter()
    # print("---->bucktetSort:", res10)

    print(res7 == res1)
