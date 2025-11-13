###
# A program that calculates the number of characters
# of your name, surname and full name
#
name = 'Paweł'  
surname = 'Wilusz' 
full_name = name + ' ' + surname
characters_in_name = len(name)
print(f'Your name has {characters_in_name} characters')
print(f'Your surname has {len(surname)} characters')
print(f'Your full name has {len(full_name)} characters') # with a space between name and surname