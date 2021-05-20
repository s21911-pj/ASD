import datetime
start_time = datetime.datetime.now()


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


arr = [14, 26, 2, 8, 13, 30, 22, 1, 24, 55, 78, 6, 444, 242, 567, 7, 44,
       33, 242, 111, 112, 114, 5557, 8, 999, 99, 15, 28, 29, 47, 84, 39, 31, 41, 32, 42, 51, 52, 58, 56, 67, 68, 622, 62, 54, 48, 21, 78]
n = len(arr)
heapSort(arr)
print(arr)
end_time = datetime.datetime.now()
elapsed_time = end_time - start_time
print(elapsed_time, ":", elapsed_time.microseconds)
