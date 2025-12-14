arr = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

print("Before:")
for row in arr:
    for val in row:
        print(val, end=" ")
    print()

# swap first and last row
temp = arr[0]
arr[0] = arr[len(arr) - 1]
arr[len(arr) - 1] = temp

print("After:")
for row in arr:
    for val in row:
        print(val, end=" ")
    print()