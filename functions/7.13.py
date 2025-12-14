def f(n):
    result = ""
    for i in range(1, n + 1):
        result += str(i)
    return result

print(f(11))  # "1234567891011"
print(f(4))   # "1234"