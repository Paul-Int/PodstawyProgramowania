import range_utils

number = int(input("A number: "))
x = 2
y = 15

result = range_utils.in_range(number, x, y)

if result:
    print(f"Number {number} in the range <{x},{y}>: yes")
else:
    print(f"Number {number} in the range <{x},{y}>: no")