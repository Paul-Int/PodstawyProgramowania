def compare(array1, array2):
    if len(array1) != len(array2):
        return False

    i = 0
    while i < len(array1):
        if array1[i] != array2[i]:
            return False
        i += 1

    return True


def print_array(label, arr):
    print(label + ":", end=" ")
    for x in arr:
        print(x, end=" ")
    print()


def print_result(same):
    if same:
        print("Comparison: arrays are the same")
    else:
        print("Comparison: arrays are different")


pairs = [
    (["water", "book", "sky"], ["water", "book", "sky"]),
    ([True, False], [True, False, True]),
    ([5, 3, 1], [5, 3, 1]),
    ([3, 2, 1], [3, 2])
]

for a1, a2 in pairs:
    print_array("Array1", a1)
    print_array("Array2", a2)
    print_result(compare(a1, a2))
    print()