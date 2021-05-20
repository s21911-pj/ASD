import datetime
start_time = datetime.datetime.now()


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


arr = [14, 26, 2, 8, 13, 30, 22, 1, 24, 55, 78, 6, 444, 242, 567, 7, 44,
       33, 242, 111, 112, 114, 5557, 8, 999, 99, 15, 28, 29, 47, 84, 39, 31, 41, 32, 42, 51, 52, 58, 56, 67, 68, 622, 62, 54, 48, 21, 78]

end_time = datetime.datetime.now()
elapsed_time = end_time - start_time
print(elapsed_time, ":", elapsed_time.microseconds)
