###
# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.
#
basic_salary = 5000
total_salary = 0
bonus = 0.30 # 30%
is_bonus = input('Does the employee receive a bonus? (Y/N):') 

if is_bonus == 'Y' or is_bonus == 'y':
    total_salary = basic_salary * (1 + bonus)
else:
    total_salary = basic_salary

print(f'Basic salary: {basic_salary}')
print('Bonus included? {yes}' if is_bonus == 'Y' else 'Bonus included? {no}')
print(f'Total salary: {total_salary}')