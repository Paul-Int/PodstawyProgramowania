###
# Calculates the total value of money spent
#
import re # module for regular expressions

# file name with shopping report
email_file = 'report.txt'

# read the content of email
with open(email_file, 'r', encoding='utf-8') as file:
   email = file.read()
# regular expression pattern
# for amounts like €30 or €120   
pattern = r'€([0-9]+(?:\.[0-9]{1,2})?)'

# extract numbers from email
# tip: findall() method returns an array
amounts = re.findall(pattern, email)

# calculate the total purchases
total = 0.0
for amount in amounts:
    total += float(amount)

# print result
print('Total money spent: €{:.2f}'.format(total))