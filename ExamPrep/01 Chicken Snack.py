from collections import deque
money = [int(x) for x in input().split()]
prices = deque(int(y) for y in input().split())
eaten_food = 0
while money and prices:
    current_money = money.pop()
    current_price = prices.popleft()
    if current_money == current_price:
        eaten_food += 1
    elif current_money > current_price:
        eaten_food += 1
        change = current_money - current_price
        if money:
            money[-1] += change
if eaten_food >= 4:
    print(f'Gluttony of the day! Henry ate {eaten_food} foods.')
elif 1 < eaten_food < 4:
    print(f'Henry ate: {eaten_food} foods.')
elif eaten_food == 1:
    print('Henry ate: 1 food.')
elif eaten_food == 0:
    print('Henry remained hungry. He will try next weekend again.')
