time=float(input('Input your time: '))

if time < 2:
    print('You have to pay 5PLN')
elif time < 6:
    print('You have to pay 15PLN')
else:
    print('You have to pay 20PLN')