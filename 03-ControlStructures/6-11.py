previous_price=200
current_price=int(input("Enter current price: "))
difference=previous_price-current_price
percent=(difference/previous_price)*100
if percent > 10:
    print(f"Current product price: {current_price}")
    print(f"Previous product price: {previous_price}")
    print("Buy the product!!!")
    print(f"The product price is reduced by {percent}%")
else:
    print("It's not worth it")
