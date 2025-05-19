import random

# Пузырьковая сортировка
def bubble_sort(arr):
    for run in range(n-1):
       for i in range(n-1-run):
           if arr[i] > arr[i + 1]:
               arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

# Быстрая сортировка
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Сортировка выбором
def selection_sort(arr):
   # Проходим по всему списку
   for i in range(len(arr)):
       # Предполагаем, что первый элемент в неотсортированной части - это минимальный
       min_index = i
       # Ищем минимальный элемент в оставшейся части списка
       for j in range(i+1, len(arr)):
           if arr[j] < arr[min_index]:
               min_index = j
       # Меняем местами найденный минимальный элемент с первым элементом в неотсортированной части
       arr[i], arr[min_index] = arr[min_index], arr[i]
   return arr

# Сортировка вставками
def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Сортировка слиянием
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    return merge(left, right)


n = 20  # количество элементов
a = -100   # минимальное значение
b = 100 # максимальное значение

name = 'Пузырьковая сортировка'
arr_random = [random.randint(a, b) for _ in range(n)]
print(f'Исходный список {arr_random}')
arr_sorted = bubble_sort(arr_random)
print(f'Результат сортировки алгоритмом {name}: {arr_sorted}')
print()
name = 'Быстрая сортировка'
arr_random = [random.randint(a, b) for _ in range(n)]
print(f'Исходный список {arr_random}')
arr_sorted = quick_sort(arr_random)
print(f'Результат сортировки алгоритмом {name}: {arr_sorted}')
print()
name = 'Сортировка выбором'
arr_random = [random.randint(a, b) for _ in range(n)]
print(f'Исходный список {arr_random}')
arr_sorted = insert_sort(arr_random)
print(f'Результат сортировки алгоритмом {name}: {arr_sorted}')
print()
name = 'Сортировка вставками'
arr_random = [random.randint(a, b) for _ in range(n)]
print(f'Исходный список {arr_random}')
arr_sorted = selection_sort(arr_random)
print(f'Результат сортировки алгоритмом {name}: {arr_sorted}')
print()
name = 'Сортировка слиянием'
arr_random = [random.randint(a, b) for _ in range(n)]
print(f'Исходный список {arr_random}')
arr_sorted = merge_sort(arr_random)
print(f'Результат сортировки алгоритмом {name}: {arr_sorted}')


