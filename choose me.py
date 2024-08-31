import time
start = time.perf_counter()
choose_sort_mas = [74, 83, -58, 27, 77, 31, 93, 26, 44, 55, -56,-7]

def choose_sort(mas):
    for i in range(len(mas)):
        min_index = i
        for j in range(i + 1, len(mas)):
            if mas[j] < mas[min_index]:
                min_index = j
        mas[i], mas[min_index] = mas[min_index], mas[i]
    return mas




print(choose_sort(choose_sort_mas))
end = time.perf_counter()
execution_time_ms = (end - start) * 1000
print("Время выполнения: ", execution_time_ms)