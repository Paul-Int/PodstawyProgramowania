list_of_numbers = [1, 2, 3, 4, 5]
with open('countries.txt', 'r') as file:
    countries = file.read()
for country in enumerate(countries.splitlines(), start=1):
    print(f"{country[0]}. {country[1]}")
    