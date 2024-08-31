import time

start = time.perf_counter()
mas = [74, 83, -58, 27, 77, 31, 93, 26, 44, 55, -56,-7]
n = len(mas)



for i in range(n - 1):
    for j in range(n - i - 1):
        if mas[j] > mas[j + 1]:
            mas[j], mas[j + 1] = mas[j + 1], mas[j]

print(mas)



end = time.perf_counter()


execution_time_ms = (end - start) * 1000
print(f"Время выполнения: {execution_time_ms:.5f}")