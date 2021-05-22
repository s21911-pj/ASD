import sys
import datetime
import random

arr1 = arr2 = arr3 = [random.randint(1, 50000) for _ in range(50000)]

arrS = []


def fillArrSort():
    for i in range(0, 5000):
        arrS.append(i)


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def build_heap(arr):
    n = len(arr)
    for i in range(n // 2-1, -1, -1):
        heapify(arr, n, i)


def heapSort(arr):
    build_heap(arr)
    n = len(arr)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


n = len(arr2)
start_time = datetime.datetime.now()
heapSort(arr2)
end_time = datetime.datetime.now()
elapsed_time = end_time - start_time


print(elapsed_time, ":", elapsed_time.microseconds)


start_time = datetime.datetime.now()

is_sorted = False
n = len(arr3)
while not is_sorted:
    is_sorted = True
    for i in range(1, n):
        if arr3[i-1] > arr3[i]:
            t = arr3[i-1]
            arr3[i-1] = arr3[i]
            arr3[i] = t
            is_sorted = False

end_time = datetime.datetime.now()
elapsed_time = end_time - start_time
print(elapsed_time, ":", elapsed_time.microseconds)

start_time = datetime.datetime.now()

sys.setrecursionlimit(100000)


def partition(arr3, low, high):
    i = (low-1)
    pivot = arr3[high]

    for j in range(low, high):

        if arr3[j] <= pivot:

            i = i+1
            arr3[i], arr3[j] = arr3[j], arr3[i]

    arr3[i+1], arr3[high] = arr3[high], arr3[i+1]
    return (i+1)


def quickSort(arr3, low, high):
    if len(arr3) == 1:
        return arr3
    if low < high:

        pi = partition(arr3, low, high)

        quickSort(arr3, low, pi-1)
        quickSort(arr3, pi+1, high)


n = len(arr3)
quickSort(arr3, 0, n-1)


end_time = datetime.datetime.now()
elapsed_time = end_time - start_time
print(elapsed_time, ":", elapsed_time.microseconds)
