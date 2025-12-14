arr = [2, 3, 7, 5, 4]

# i. the array
print("Array:", arr)

# ii. number of elements
print("Number of elements:", len(arr))

# iii. first value
print("First value:", arr[0])

# iv. second value
print("Second value:", arr[1])

# v. last value
print("Last value:", arr[len(arr) - 1])

# vi. last but one value (bez indeksów ujemnych)
print("Last but one value:", arr[len(arr) - 2])

# vii. sum of the first and last value
print("Sum of first and last value:", arr[0] + arr[len(arr) - 1])

# viii. middle value
middle_index = len(arr) // 2
print("Middle value:", arr[middle_index])

# ix. all array values separated by a single space (loop)
print("All values:", end=" ")
for value in arr:
    print(value, end=" ")
print()