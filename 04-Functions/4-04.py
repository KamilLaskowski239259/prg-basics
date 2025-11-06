###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    sum = 0
    
    for i in range(len(str(number))):  
        sum += int(str(number)[i])
    return sum

any_number = int(input('Enter integer number: '))

result = sum_digits(abs(any_number))

print(f'The sum of the digits in the number {any_number} is {result}.')
