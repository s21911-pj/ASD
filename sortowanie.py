import datetime
start_time = datetime.datetime.now()

tablica = [14, 26, 2, 8, 13, 30, 22, 1, 24, 55, 78, 6, 444, 242, 567, 7, 44,
           33, 242, 111, 112, 114, 5557, 8, 999, 99, 15, 28, 29, 47, 84, 39, 31, 41, 32, 42, 51, 52, 58, 56, 67, 68, 622, 62, 54, 48, 21, 78]
is_sorted = False
n = len(tablica)
while not is_sorted:
    is_sorted = True
    for i in range(1, n):
        if tablica[i-1] > tablica[i]:
            t = tablica[i-1]
            tablica[i-1] = tablica[i]
            tablica[i] = t
            is_sorted = False
print(tablica)
end_time = datetime.datetime.now()
elapsed_time = end_time - start_time
print(elapsed_time, ":", elapsed_time.microseconds)
