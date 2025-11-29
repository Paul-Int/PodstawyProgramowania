###
# Calculates the sum of even numbers from 1 to a given number N
#
N = 30
sum_even = 0

# Calculate the sum of even numbers
while N < 1:
    N = int(input("Enter a positive integer N: "))
for i in range(1, N + 1):
    if i % 2 == 0:
        sum_even += i

print(f"The sum of even numbers from 1 to {N} is: {sum_even}")