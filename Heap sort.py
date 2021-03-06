import datetime
import random


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


arr = [random.randint(1, 50000) for _ in range(50000)]
n = len(arr)
start_time = datetime.datetime.now()
heapSort(arr)
end_time = datetime.datetime.now()
elapsed_time = end_time - start_time
print(elapsed_time.seconds, ":", elapsed_time.microseconds)
print("end first sorting")
start_time = datetime.datetime.now()
arr.reverse()
start_time = datetime.datetime.now()
heapSort(arr)
end_time = datetime.datetime.now()
elapsed_time = end_time - start_time
print(elapsed_time.seconds, ":", elapsed_time.microseconds)
print("end second sorting")
arr.sort()
start_time = datetime.datetime.now()
heapSort(arr)
end_time = datetime.datetime.now()
elapsed_time = end_time - start_time
print(elapsed_time.seconds, ":", elapsed_time.microseconds)
print("end third sorting")
