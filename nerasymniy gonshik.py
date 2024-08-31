import time

mas = [74, 83, -58, 27, 77, 31, 93, 26, 44, 55, -56,-7]  # Быстрая сортировка



def quick_sort(mas):
    if len(mas) <= 1:
        return mas

    element = mas[0]
    left = list(filter(lambda x: x < element, mas))
    center = [i for i in mas if i == element]
    right = list(filter(lambda x: x > element, mas))

    return quick_sort(left) + center + quick_sort(right)

start = time.perf_counter()
print(quick_sort(mas))
end = time.perf_counter()
execution_time_ms = (end - start) * 1000
print(f"Время выполнения: {execution_time_ms:.5f}")