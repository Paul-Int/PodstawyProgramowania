arr = [[-38, 19], [5, 40], [-7, 11], [29, 16]]

min_val = arr[0][0]
max_val = arr[0][0]
min_row = 0
min_col = 0
max_row = 0
max_col = 0

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] < min_val:
            min_val = arr[i][j]
            min_row = i
            min_col = j
        if arr[i][j] > max_val:
            max_val = arr[i][j]
            max_row = i
            max_col = j

print("Min value:", min_val, "at row", min_row + 1, "col", min_col + 1)
print("Max value:", max_val, "at row", max_row + 1, "col", max_col + 1)