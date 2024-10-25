import timeit
import random

# Алгоритм сортування злиттям
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Знаходимо середину масиву
    mid = len(arr) // 2
    # Розбиваємо масив на дві половини
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Рекурсивно сортуємо обидві половини та об'єднуємо
    return merge(merge_sort(left_half), merge_sort(right_half))

# Функція об'єднання двох відсортованих масивів
def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Порівнюємо елементи в лівому та правому масивах
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Додаємо залишки з лівого масиву
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    # Додаємо залишки з правого масиву
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

# Алгоритм сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Переміщуємо елементи, які більші за key, вправо
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Вставляємо елемент у правильне місце
        arr[j + 1] = key

    return arr

# Використовуємо вбудовану функцію Python (Timsort)
def tim_sort(arr):
    return sorted(arr)

# Функція для вимірювання часу виконання алгоритму
def measure_time(sort_func, arr):
    start_time = timeit.default_timer()
    sort_func(arr.copy())
    end_time = timeit.default_timer()
    return end_time - start_time

# Тестові масиви для аналізу
small_array = random.sample(range(0, 1000), 100)  # Малий масив (100 елементів)
medium_array = random.sample(range(0, 10000), 1000)  # Середній масив (1000 елементів)
large_array = random.sample(range(0, 100000), 10000)  # Великий масив (10,000 елементів)

# Емпіричний аналіз часу виконання
print("Час сортування на малому масиві (100 елементів):")
print(f"Merge Sort: {measure_time(merge_sort, small_array):.5f} сек")
print(f"Insertion Sort: {measure_time(insertion_sort, small_array):.5f} сек")
print(f"Timsort: {measure_time(tim_sort, small_array):.5f} сек")

print("\nЧас сортування на середньому масиві (1000 елементів):")
print(f"Merge Sort: {measure_time(merge_sort, medium_array):.5f} сек")
print(f"Insertion Sort: {measure_time(insertion_sort, medium_array):.5f} сек")
print(f"Timsort: {measure_time(tim_sort, medium_array):.5f} сек")

print("\nЧас сортування на великому масиві (10,000 елементів):")
print(f"Merge Sort: {measure_time(merge_sort, large_array):.5f} сек")
print(f"Insertion Sort: {measure_time(insertion_sort, large_array):.5f} сек")
print(f"Timsort: {measure_time(tim_sort, large_array):.5f} сек")
