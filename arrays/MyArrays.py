# MyArrays.py

def second_largest(arr):
    max_val = arr[0]
    for x in arr:
        if x > max_val:
            max_val = x

    second = None
    for x in arr:
        if x != max_val:
            if second is None or x > second:
                second = x

    return second


def diff_max_min(arr):
    max_val = arr[0]
    min_val = arr[0]

    for x in arr:
        if x > max_val:
            max_val = x
        if x < min_val:
            min_val = x

    return max_val - min_val


def median(arr):
    a = arr[:]
    n = len(a)

    # bubble sort
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp

    return a[n // 2]


def min_max_array(arr):
    min_val = arr[0]
    max_val = arr[0]

    for x in arr:
        if x < min_val:
            min_val = x
        if x > max_val:
            max_val = x

    return [min_val, max_val]


def array_to_string(arr):
    result = ""
    i = 0
    while i < len(arr):
        result += str(arr[i])
        if i < len(arr) - 1:
            result += "-"
        i += 1
    return result