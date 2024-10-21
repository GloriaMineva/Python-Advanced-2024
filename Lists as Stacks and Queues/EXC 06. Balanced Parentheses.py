from collections import deque
parentheses_deque = deque(input())
opening_parentheses = deque()
while parentheses_deque:
    current_parentheses = parentheses_deque.popleft()
    if current_parentheses in '([{':
        opening_parentheses.append(current_parentheses)
    elif not opening_parentheses:
        print('NO')
        break
    else:
        current_combination = opening_parentheses.pop() + current_parentheses
        if current_combination not in '(){}[]':
            print('NO')
            break
else:
    print('YES')

