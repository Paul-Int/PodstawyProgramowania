import MyArrays

numbers = [7, 3, 8, 5, 2]

print("Numbers:", end=" ")
for x in numbers:
    print(x, end=" ")
print()

print("Second largest number:", MyArrays.second_largest(numbers))
print("Median:", MyArrays.median(numbers))

min_max = MyArrays.min_max_array(numbers)
print("Smallest and largest number:", min_max[0], ",", min_max[1])

print("Numbers as a string:", MyArrays.array_to_string(numbers))