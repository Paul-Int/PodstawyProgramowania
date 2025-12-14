a = [2, 4, 6]
b = [1, 2, 3, 4, 5, 6, 7]

is_subset = True

for x in a:
    found = False
    for y in b:
        if x == y:
            found = True
    if not found:
        is_subset = False

print("Array A:", a)
print("Array B:", b)

if is_subset:
    print("Array A is a subset of Array B")
else:
    print("Array A is NOT a subset of Array B")