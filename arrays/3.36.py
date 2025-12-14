def to_1d_array(m):
    arr = []
    for row in m:
        for val in row:
            arr.append(val)
    return arr

a1 = [
    [2, 3],
    [1, 5]
]

print("1D array:", to_1d_array(a1))

a2 = [
    [5, 0, 3, 7, 5],
    [9, 0, 9, 1, 2]
]

print("1D array:", to_1d_array(a2))

a3 = [
    [2, 1],
    [3, 5],
    [7, 4],
    [2, 6]
]

print("1D array:", to_1d_array(a3))