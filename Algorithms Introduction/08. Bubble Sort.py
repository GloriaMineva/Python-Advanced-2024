def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


numbers_to_sort = list(map(int, input().split()))
bubble_sort(numbers_to_sort)
print(*numbers_to_sort)