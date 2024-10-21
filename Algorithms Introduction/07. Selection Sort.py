def selection_sort(numbers_):
    for i in range(len(numbers_)):
        min_index = i
        for j in range(i + 1, len(numbers_)):
            if numbers_[j] < numbers_[min_index]:
                min_index = j
        numbers_[i], numbers_[min_index] = numbers_[min_index], numbers_[i]


numbers_to_sort = list(map(int, input().split()))
selection_sort(numbers_to_sort)
print(*numbers_to_sort)