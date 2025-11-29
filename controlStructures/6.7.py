###
age_group = ""
age = int(input("Enter your age: "))
if age < 13:
    age_group = "child"
elif age >= 13 and age <=19:
    age_group = "teen"
elif age >= 20 and age <= 64:
    age_group = "adult"
else:
    age_group = "senior"
print(f'Your age group is: {age_group}')        