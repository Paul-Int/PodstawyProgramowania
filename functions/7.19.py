def f(number):
    seen = set()
    total = 0

    for ch in str(number):
        if ch in seen:
            total += int(ch)
        else:
            seen.add(ch)

    return total

print(f(1027))
print(f(230335))
print(f(513553007))