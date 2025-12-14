def f(name):
    words = name.split()
    result = ""
    for w in words:
        result += w[0]
    return result

print(f("Internet of Things"))
print(f("For Your Information"))
print(f("Python"))