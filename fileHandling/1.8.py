
def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content
    
file_content = read_from_file('pets.txt')
file_lines = file_content.splitlines()
    
for line in file_lines:
    line.split()
    summed_words = sum(len(line) - line.count(' ') for line in file_lines)
    print(line)
print('Total number of characters in pets.txt:', summed_words)