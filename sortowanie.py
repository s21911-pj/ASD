import datetime
import random
start_time = datetime.datetime.now()

tablica = [random.randint(1, 50000) for _ in range(50000)]
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

end_time = datetime.datetime.now()
elapsed_time = end_time - start_time
print(elapsed_time.seconds, ":", elapsed_time.microseconds)

tablica.sort()
start_time = datetime.datetime.now()
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

end_time = datetime.datetime.now()
elapsed_time = end_time - start_time
print(elapsed_time.seconds, ":", elapsed_time.microseconds)

tablica.reverse()
start_time = datetime.datetime.now()
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

end_time = datetime.datetime.now()
elapsed_time = end_time - start_time
print(elapsed_time.seconds, ":", elapsed_time.microseconds)
