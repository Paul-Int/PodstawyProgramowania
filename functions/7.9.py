def f(number, even):
    s = 0
    for d in str(number):
        digit = int(d)
        if even and digit % 2 == 0:
            s += digit
        if not even and digit % 2 == 1:
            s += digit
    return s

print(f(3124, True))    # 6
print(f(3124, False))   # 4
print(f(20576, False))  # 12
print(f(20576, True))   # 8
print(f(13115, True))   # 0