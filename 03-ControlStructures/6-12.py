number_products=int(input('How many products: '))
price=int(input("Price: "))
if number_products > 2:
    amount_to_pay = ((price*(number_products-2))*0.75)+(2*price)
else:
    amount_to_pay = number_products*price
print(f'You have to pay: {amount_to_pay}')