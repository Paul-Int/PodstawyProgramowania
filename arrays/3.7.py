names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

longest = names[0]
for name in names:
    if len(name) > len(longest):
        longest = name

print("Names:", end=" ")
for n in names:
    print(n, end=" ")
print()

print("Longest name:", longest)