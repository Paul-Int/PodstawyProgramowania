###
# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.   
# 
import math
number1 = float( input ('Enter first number: '))
number2 = float( input ('Enter second number: '))
operator = input ('Enter operator (+, -, *, /): ')

if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == '*':
    result = number1 * number2
elif operator == '/':
    result = number1 / number2
else:
    result = 'Incorrect operator'

# print result
print(f'The result of {number1} {operator} {number2} is: {result}')