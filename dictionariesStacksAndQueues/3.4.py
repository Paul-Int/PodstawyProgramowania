n = int(input("Natural number: "))

if n == 0:
    print("Binary number: 0")
else:
    stack = []
    number = n

    while number > 0:
        remainder = number % 2
        stack.append(remainder)   # push remainder
        number = number // 2      # integer division

    binary = ""
    while stack:
        binary += str(stack.pop())  # pop and build binary string

    print("Binary number:", binary)