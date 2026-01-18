import csv

# Read provinces mapping: letter -> province name
letter_to_province = {}
with open("province.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        letter_to_province[row["Letter"].strip()] = row["Name"].strip()

# Init counts for each province
province_counts = {province: 0 for province in letter_to_province.values()}

# Count vehicles by first letter of registration
with open("vehicle.txt", "r", encoding="utf-8") as f:
    for line in f:
        reg = line.strip()
        if not reg:
            continue

        first_letter = reg[0].upper()
        if first_letter in letter_to_province:
            province = letter_to_province[first_letter]
            province_counts[province] += 1

# Print results
for province, count in province_counts.items():
    print(province, ":", count)