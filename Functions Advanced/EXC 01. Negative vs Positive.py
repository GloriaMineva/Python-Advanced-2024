def positive_negative_sorter(raw_data: str):
    numbers = [int(el) for el in raw_data.split()]
    positive_sum = sum(el for el in numbers if el > 0)
    negative_sum = sum(el for el in numbers if el < 0)
    print(negative_sum)
    print(positive_sum)
    if abs(negative_sum) > positive_sum:
        print('The negatives are stronger than the positives')
    else:
        print('The positives are stronger than the negatives')


positive_negative_sorter(input())