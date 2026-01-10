###
# Prints employees employed in a specified position.
#

# Employee List
file_name = 'it_company.csv'

# Position
job_title = 'Software Engineer'

def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content

file_content = read_from_file('it_company.csv')
file_lines = file_content.splitlines()

i = 1

for line in file_lines:        
    if job_title in line:
        line = line.replace(',', ', ')
        print(f"{i}. {line}")
        i += 1

        