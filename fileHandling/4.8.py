import re

with open("files.txt", "r") as file:
    for line in file:
        name = line.strip()
        if re.search(r"\.[A-Za-z0-9]{4}$", name):
            print(name)