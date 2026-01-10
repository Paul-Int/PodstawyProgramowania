###
# Saves to a file a list of employees working at a specified position.
#

# file names
employees_file = 'it_company.csv'
position_file = 'software_engineer.txt'

# Position
job_title = 'Software Engineer'

# write selected employees to a file
def read_from_file(employees_file):
   with open(employees_file, 'r') as file:
      content = file.read()
   return content

with open(position_file, 'w') as file:
    for line in read_from_file(employees_file).splitlines():
        if job_title in line:
            line = line.replace(',', ', ')
            file.write(f"{line}\n")