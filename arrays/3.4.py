arr = [-15, 8, -31, 47, -2, 19]

min_val = arr[0]
max_val = arr[0]

i = 1
while i < len(arr):
    if arr[i] < min_val:
        min_val = arr[i]
    if arr[i] > max_val:
        max_val = arr[i]
    i += 1

print("Minimum:", min_val)
print("Maximum:", max_val)