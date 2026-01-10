file = open("it_company.csv", "r", encoding="utf-8")

header = file.readline() 

print("GRAPHIC DESIGNERS")
print("=================")

for line in file:
    line = line.strip()
    parts = line.split(",")

    last_name = parts[0]
    first_name = parts[1]
    job_title = parts[2]
    email = parts[3]

    if job_title == "Graphic Designer":
        print(first_name + " " + last_name + "," + email)

file.close()