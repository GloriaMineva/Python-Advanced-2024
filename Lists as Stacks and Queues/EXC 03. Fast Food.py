from collections import deque

quantity_food = int(input())
orders_deque = deque(input().split())
orders_deque = deque(int(x) for x in orders_deque)  # generator comprehension to int
# is more efficient than list to deque convertion
biggest_order = max(orders_deque)
print(biggest_order)
while orders_deque:
    if orders_deque[0] <= quantity_food:
        quantity_food -= orders_deque.popleft()
    else:
        print(f'Orders left:', *orders_deque)
        break

else:
    print('Orders complete')
