arr = [2, 3, 2, 5, 8, 1, 9, 8]

print("Array:", end=" ")
for x in arr:
    print(x, end=" ")
print()

print("Unique elements:", end=" ")
for x in arr:
    count = 0
    for y in arr:
        if x == y:
            count += 1
    if count == 1:
        print(x, end=" ")
print()