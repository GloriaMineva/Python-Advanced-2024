from collections import deque
strength = [int(el) for el in input().split()]
accuracy = deque(int(x) for x in input().split())
goals = 0

while strength and accuracy:
    curr_strength = strength.pop()
    curr_accuracy = accuracy.popleft()
    if curr_accuracy + curr_strength == 100:
        goals += 1
    elif curr_accuracy + curr_strength < 100:
        if curr_strength < curr_accuracy:
            accuracy.appendleft(curr_accuracy)
        elif curr_strength > curr_accuracy:
            strength.append(curr_strength)
        elif curr_accuracy == curr_strength:
            new_strength = curr_strength + curr_accuracy
            strength.append(new_strength)
    elif curr_accuracy + curr_strength > 100:
        curr_strength -= 10
        if curr_strength > 0:
            strength.append(curr_strength)
        else:
            curr_strength = 0
            strength.append(curr_strength)
        accuracy.append(curr_accuracy)
if goals == 3:
    print("Paul scored a hat-trick!")
elif goals > 3:
    print("Paul performed remarkably well!")
elif 1 <= goals < 3:
    print("Paul failed to make a hat-trick.")
elif goals == 0:
    print("Paul failed to score a single goal.")
if goals > 0:
    print(f"Goals scored: {goals}")
if strength:
    print(f'Strength values left: {", ".join(map(str, strength))}')
if accuracy:
    print(f'Accuracy values left: {", ".join(map(str, accuracy))}')




