###
# a program that converts decimal number to binary and hexadecimal
#
decimal = int(input('Enter a decimal number: '))
binary = bin(int(decimal))
hexadecimal = hex(int(decimal))
print(f'Binary number: {binary} ')
print(f'Hexadecimal number: {hexadecimal} ')
