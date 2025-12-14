matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# replace main diagonal values with 1
for i in range(len(matrix)):
    matrix[i][i] = 1

# print modified array
for row in matrix:
    for value in row:
        print(value, end=" ")
    print()