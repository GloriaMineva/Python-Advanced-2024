from collections import deque
user_data = deque(input().split())
user_data.reverse()
print(' '.join(user_data))



# user_data = list(input().split(' '))
# while user_data:
#     print(user_data.pop(), end=' ')