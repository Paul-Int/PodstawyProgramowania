basic_data = {
    "name": "Barbara",
    "age": 21
}

advanced_data = {
    "status": "student",
    "married": False,
    "interest": ["reading", "swimming"]
}

# create person dictionary with data from both dictionaries
person = {}

person.update(basic_data)
person.update(advanced_data)

# print contents of person dictionary
print(person)