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

# swap first and last column in each row
for i in range(len(arr)):
    temp = arr[i][0]
    arr[i][0] = arr[i][len(arr[i]) - 1]
    arr[i][len(arr[i]) - 1] = temp

print("After:")
for row in arr:
    for val in row:
        print(val, end=" ")
    print()