
file = open('it_company.csv', 'r')

count = 0
lines = file.readlines()
total = len(lines)

for i in range(total):
    print(lines[i].rstrip())
    count += 1

    if count == 5 and i != total - 1:
        input("Press Enter key...")
        count = 0

file.close()




    
    