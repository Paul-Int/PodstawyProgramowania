###
# A program that enables a user to challenge a computer.
# The computer throws dice. Then, the user then tries to guess
# the number from dice by entering a number from 1 to 6
# from the keyboard. If the user has guessed the number
# from the dice, the computer prints True. Otherwise,
# the computer prints False.
#
import random
# COMPUTER TURN
computer = random.randint(1,6)
# YOUR TURN
you = input(f'Guess the number from dice roll (1-6): ')
you_int = int(you)
print(f'You won: {you_int == computer}')
print(f'Computer rolled: {computer}')