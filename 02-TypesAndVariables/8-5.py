###
# A program that reads a SWIFT code from the keyboard
# and prints the bank code and country code.
#
swift = input('Input your SWIFT code: ')
bank_code=swift[0:3]
country_code=swift[3:5]
print(f'Bank Code: {bank_code}')
print(f'Country Code: {country_code}')