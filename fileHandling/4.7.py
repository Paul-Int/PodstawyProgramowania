import re

text = input("Enter text: ")

vowels = re.findall(r"[aeiouyAEIOUY]", text)
print("Number of vowels:", len(vowels))