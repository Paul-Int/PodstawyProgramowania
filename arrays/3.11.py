def bubblesort(array):
    arr = array[:]          # kopia, żeby nie psuć oryginału
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

    return arr


a = [5, 1, 4, 2, 8]
b = [10, -3, 7, 7, 2]
c = [9, 0, 3, 6, 1]

print("Array:", a)
print("Sorted:", bubblesort(a))
print()

print("Array:", b)
print("Sorted:", bubblesort(b))
print()

print("Array:", c)
print("Sorted:", bubblesort(c))