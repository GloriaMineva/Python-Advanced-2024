def recursive_drawer(n):
    if n == 0:
        return
    print('*' * n)
    recursive_drawer(n - 1)
    print('#' * n)

recursive_drawer(int(input()))
