def coins_counter(lst_coins:list, desired_sum_:int):
    counter = 0
    used_coins_and_count = {}
    for el in lst_coins:
        current_coin_count = desired_sum_ // el
        used_coins_and_count[el] = current_coin_count
        desired_sum_ = desired_sum_ % el
        counter += current_coin_count
        if desired_sum_ == 0:
            print(f'Number of coins to take: {counter}')
            for k, v in used_coins_and_count.items():
                if not v == 0:
                    print(f'{v} coin(s) with value {k}')
            return
    if not desired_sum_ == 0:
        print('Error')
         


coins = list(map(int, input().split(', ')))
coins = sorted(coins, reverse=True)
desired_sum = int(input())
coins_counter(coins, desired_sum)