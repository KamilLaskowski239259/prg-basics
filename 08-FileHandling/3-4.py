###
# Calculates the total value of money spent
#
import re # module for regular expressions

# file name with shopping report
email_file = 'report.txt'

# read the content of email
open(email_file)
...
email = ... (email content)

# regular expression pattern
# for amounts
pattern = '....'

# extract numbers from email
# tip: findall() method returns an array
amounts = re.findall(pattern, email)

# calculate the total purchases
...
for amount in amounts:
   ...

# print result
print(...)