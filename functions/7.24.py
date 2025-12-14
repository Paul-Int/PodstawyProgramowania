def f(expression):
    total = 0
    sign = 1
    for ch in expression:
        if ch == "+":
            sign = 1
        elif ch == "-":
            sign = -1
        else:
            total += sign * int(ch)
    return total

print(f("2+3"))
print(f("3+8+1"))
print(f("2+3-4+5-0"))