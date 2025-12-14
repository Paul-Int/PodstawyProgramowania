def identity_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix

def print_matrix(m):
    for row in m:
        for val in row:
            print(val, end=" ")
        print()
        
print("Identity matrix 3x3:")
print_matrix(identity_matrix(3))
print()

print("Identity matrix 5x5:")
print_matrix(identity_matrix(5))
print()

print("Identity matrix 8x8:")
print_matrix(identity_matrix(8))