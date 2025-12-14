arr = [2.5, 4.1, 6.7, 1.2, 8.9, 3.0]
value = float(input("Enter value: "))

count = 0
for x in arr:
    if x > value:
        count += 1

print("Array:", arr)
print("Number of elements greater than", value, ":", count)