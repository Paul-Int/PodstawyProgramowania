t = (50, 20, 40, 50, 30, 50)
value = 50

count = 0
for x in t:
    if x == value:
        count += 1

print("Tuple:", end=" ")
for x in t:
    print(x, end=" ")
print()

print("Value:", value)
print("Number of occurrences:", count)