def occurs(number, array):
    for x in array:
        if x == number:
            return True
    return False


arr = [15, 38, 7, 23, 14]
num = int(input("Number: "))

print("Array:", end=" ")
for x in arr:
    print(x, end=" ")
print()

if occurs(num, arr):
    print("Result: number", num, "appears in the array")
else:
    print("Result: number", num, "does not appear in the array")