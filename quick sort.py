import datetime
import random


def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)


def partition(A, p, r):
    pivot = A[r]
    smaller = p
    for j in range(p, r):
        if A[j] <= pivot:
            A[smaller], A[j] = A[j], A[smaller]
            smaller = smaller + 1
    A[smaller], A[r] = A[r], A[smaller]
    return smaller


arr3 = [random.randint(1, 50000) for _ in range(50000)]
print("tab 3", len(arr3))
start_time = datetime.datetime.now()
quick_sort(arr3, 0, len(arr3)-1)
end_time = datetime.datetime.now()
elapsed_time = end_time - start_time
print(elapsed_time.seconds, ".", elapsed_time.microseconds)
