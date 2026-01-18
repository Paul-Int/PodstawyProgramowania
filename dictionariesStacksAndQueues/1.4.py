person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming", "excursions"],
    "married": True,
    "phone": {
        "landline": "123444321",
        "mobile": "777888999"
    }
}

# i. Displays name
print(person["name"])

# ii. Displays hobby
print(person["hobby"])

# iii. Displays the entire dictionary
print(person)

# iv. Changes surname to 'Nowak'
person["surname"] = "Nowak"

# v. Changes person's marriage status
person["married"] = False

# vi. Adds gender: 'male'
person["gender"] = "male"

# vii. Adds a new hobby: 'bicycle'
person["hobby"].append("bicycle")

# viii. Adds work phone to existing phones
person["phone"]["work"] = "313131444"

# ix. Displays the entire contents of the dictionary (iterate over items)
for key, value in person.items():
    print(f"{key}: {value}")
