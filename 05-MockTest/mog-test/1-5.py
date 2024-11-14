def f(binary_number):
    return all(char in '01' for char in binary_number)
number=input("Enter number: ")
result=f(number)
print(result)