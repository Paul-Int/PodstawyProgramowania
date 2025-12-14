def f(n):
    if n == 1:
        return 0
    if n == 2:
        return 1

    a = 0
    b = 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

print(f(5)) # 3
print(f(9)) # 21