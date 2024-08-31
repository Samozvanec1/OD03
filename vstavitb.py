import time

insert_sort_mas = [74, 83, -58, 27, 77, 31, 93, 26, 44, 55, -56,-7]  #Cортировка вставкой


def insert_sort(mas):
    for i in range(1, len(mas)):
        temp = mas[i]
        j = i - 1
        while j >= 0 and temp < mas[j]:
            mas[j + 1] = mas[j]
            j -= 1
        mas[j + 1] = temp
    return mas

start = time.perf_counter()
print(insert_sort(insert_sort_mas))
end = time.perf_counter()
execution_time_ms = (end - start) * 1000
print("Время выполнения: ", execution_time_ms)
