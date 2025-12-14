def f(dice):
    best = 0
    current = 0
    prev = ""
    for ch in dice:
        if ch == prev:
            current += 1
        else:
            current = 1
            prev = ch
        if current > best:
            best = current
    return best

print(f("52331655554211"))
print(f("2133"))
