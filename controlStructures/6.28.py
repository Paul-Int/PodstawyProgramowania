a = 0
b = 1

print(a, b, end=" ")

count = 2

while count < 20:
    c = a + b
    print(c, end=" ")
    a = b
    b = c
    count = count + 1