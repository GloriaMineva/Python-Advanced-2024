def binary_search(numbers_, element_):
    left_idx = 0
    right_idx = len(numbers_) - 1
    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2
        if element_ == numbers_[mid_idx]:
            return mid_idx
        elif element_ > numbers_[mid_idx]:
            left_idx = mid_idx + 1
        else:
            right_idx = mid_idx - 1
    return -1



numbers = list(map(int, input().split()))
element_to_find = int(input())
print(binary_search(numbers, element_to_find))