# all_customers = []
# while True:
#     current_customer = input()
#     all_customers.append(current_customer)
#     if current_customer == 'Paid':
#         all_customers.pop()
#         while all_customers:
#             print(all_customers.pop(0))
#     elif current_customer == 'End':
#         all_customers.pop()
#         print(f'{len(all_customers)} people remaining.')
#         break


# from collections import deque
# all_customers = deque()
# while True:
#     current_customer = input()
#     all_customers.append(current_customer)
#     if current_customer == 'Paid':
#         all_customers.pop()
#         while all_customers:
#             print(all_customers.popleft())
#     elif current_customer == 'End':
#         all_customers.pop()
#         print(f'{len(all_customers)} people remaining.')
#         break

from queue import Queue
all_customers = Queue(maxsize=10)
while True:
    current_customer = input()
    if current_customer == 'Paid':
        while all_customers:
            print(all_customers.get())
    if current_customer == 'End':
        print(f'{all_customers.qsize()} people remaining.')
        break
    all_customers.put(current_customer)