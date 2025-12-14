def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

# program – obliczenie 5^3
print(power(5, 3))   # 125