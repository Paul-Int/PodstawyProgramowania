def create_2d_arr(x, y):
    arr = []
    for i in range(x):
        row = []
        for j in range(y):
            row.append(0)
        arr.append(row)
    return arr

a = create_2d_arr(3, 5)

for row in a:
    for val in row:
        print(val, end=" ")
    print()