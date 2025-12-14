arr1 = [4, 36, 12, 28, 9, 44, 5]
arr2 = [5, 1, 36]

print("Array1:", arr1)
print("Array2:", arr2)
print("Not in Array2:", end=" ")

for x in arr1:
    found = False
    for y in arr2:
        if x == y:
            found = True
    if not found:
        print(x, end=" ")
print()