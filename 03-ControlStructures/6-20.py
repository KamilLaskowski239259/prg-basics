decimal=int(input("Enter a decimal number: "))
reminders = []
original = decimal
while decimal > 0:
    reminder = decimal%2
    reminders.append(reminder)
    decimal = decimal // 2
binary_number = ''.join(map(str, reminders[::-1]))
print(f"{original}(10)={binary_number}(2)")