##
# program thath tells if a tree can be cut down
#

height = input('Enter tree circumference in cm: ')
can_be_cut = int(height) >= 50  
print(f'Tree can be cut down: {can_be_cut}')