t = (10, 20, 30, 40, 50)

print("Tuple:", end=" ")
for x in t:
    print(x, end=" ")
print()

print("Reverse order:", end=" ")
i = len(t) - 1
while i >= 0:
    print(t[i], end=" ")
    i -= 1
print()