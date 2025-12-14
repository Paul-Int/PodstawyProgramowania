###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    total = 0
    for digit in str(number):
        total += int(digit)
    return total

any_number = int(input('Enter integer number: '))
if any_number < 0:
    any_number = abs(any_number)
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')