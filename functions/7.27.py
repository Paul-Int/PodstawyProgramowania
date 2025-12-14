def f(code):
    if len(code) != 4 or not code.isdigit():
        return False
    s = int(code[0]) + int(code[1]) + int(code[2])
    return s % 7 == int(code[3])

print(f("1082"))
print(f("2035"))
print(f("1114"))
print(f("7071"))