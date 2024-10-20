Price=float(input("Enter price: "))
Prercent=float(input("Enter discount in %: "))

Discount=Prercent/100
Difference=Price*Discount
Price_After=Price-Difference

print(f"Price is {Price}")
print(f"The discount is {Prercent}%")
print(f"Price after the discount is {Price_After}")
print(f"The difference in prices is {Difference}")