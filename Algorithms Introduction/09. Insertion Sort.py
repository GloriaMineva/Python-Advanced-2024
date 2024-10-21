def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = key



numbers_to_sort = list(map(int, input().split()))
insertion_sort(numbers_to_sort)
print(*numbers_to_sort)