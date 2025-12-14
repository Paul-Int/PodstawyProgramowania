def transpose_matrix(m):
    rows = len(m)
    cols = len(m[0])
    t = []

    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(m[i][j])
        t.append(row)

    return t

m1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
def print_matrix(m):
    for row in m:
        for val in row:
            print(val, end=" ")
        print()
    print()

print("Original:")
print_matrix(m1)
print("Transposed:")
print_matrix(transpose_matrix(m1))
print()

m2 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0]
]

print("Original:")
print_matrix(m2)
print("Transposed:")
print_matrix(transpose_matrix(m2))
print()

m3 = [
    [5, 6, 7, 8]
]

print("Original:")
print_matrix(m3)
print("Transposed:")
print_matrix(transpose_matrix(m3))
print()
