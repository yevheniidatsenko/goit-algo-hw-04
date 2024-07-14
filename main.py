import timeit
import random

def merge_sort(arr):
    """Merge sort algorithm"""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result

def insertion_sort(arr):
    """Insertion sort algorithm"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def timsort(arr):
    """Timsort algorithm (using Python's built-in sorted function)"""
    return sorted(arr)

# Generate random data sets of different sizes
data_sizes = [100, 1000, 10000, 100000]
for size in data_sizes:
    arr = [random.randint(0, 100) for _ in range(size)]

    # Time merge sort
    start_time = timeit.default_timer()
    merge_sort(arr.copy())
    merge_sort_time = timeit.default_timer() - start_time

    # Time insertion sort
    start_time = timeit.default_timer()
    insertion_sort(arr.copy())
    insertion_sort_time = timeit.default_timer() - start_time

    # Time Timsort
    start_time = timeit.default_timer()
    timsort(arr.copy())
    timsort_time = timeit.default_timer() - start_time

    print(f"Data size: {size}")
    print(f"Merge sort time: {merge_sort_time:.6f} seconds")
    print(f"Insertion sort time: {insertion_sort_time:.6f} seconds")
    print(f"Timsort time: {timsort_time:.6f} seconds")
    print()

# Висновки:
# Результати показують, що Timsort значно швидший за сортування злиттям та сортування вставкою для великих масивів даних.
# Це пояснюється тим, що Timsort використовує сильні сторони сортування злиттям та сортування вставкою, використовуючи сортування вставкою для малих масивів та сортування злиттям для великих масивів.
# Гібридний підхід Timsort робить його більш ефективним і практичним вибором для сортування великих масивів даних у Python.