def recursive_sum(array_of_nums, idx):
    if idx == len(array_of_nums) - 1:
        return array_of_nums[idx]
    return array_of_nums[idx] + recursive_sum(array_of_nums, idx + 1)


numbers = list(map(int, input().split()))
print(recursive_sum(numbers, 0))

# def recursive_sum(array_of_nums, idx):
#     sum_recursion = 0
#     if idx == len(array_of_nums):
#         return sum_recursion
#     sum_recursion = array_of_nums[idx] + recursive_sum(array_of_nums, idx + 1)
#     return sum_recursion
#
#
# numbers = list(map(int, input().split()))
# print(recursive_sum(numbers, 0))


