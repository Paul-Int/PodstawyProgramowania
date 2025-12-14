arr = [1, 2, 3, 4, 5]

print("Array:", arr)

# i. subtract one from the first element
arr[0] = arr[0] - 1
print("Array:", arr)

# ii. increase the last array element by 4
arr[len(arr) - 1] = arr[len(arr) - 1] + 4
print("Array:", arr)

# iii. multiply the middle array element by 2
middle_index = len(arr) // 2
arr[middle_index] = arr[middle_index] * 2
print("Array:", arr)