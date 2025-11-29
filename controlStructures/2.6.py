###
# program that checks what number was entered from the keyboard and prints one 
# of the following messages:

number = int(input('Enter a number: '))

if number > 0:
    print(f'the number {number} is positive')
elif number < 0:
    print(f'the number {number} is negative')
else:
    print('The number is zero')
