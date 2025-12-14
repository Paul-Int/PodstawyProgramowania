arr = [2, 6, 4, 9, 7]

def star(n):
    s = ""
    i = 0
    while i < n:
        s += "*"
        i += 1
    return s

for x in arr:
    print(str(x) + ":", star(x))