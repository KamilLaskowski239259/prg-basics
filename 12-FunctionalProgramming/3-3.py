stock = [(20,5.50),(15,8.30),(37,3.85),(4,11.60)]
prices=list(map(lambda item:item[0]*item[1],stock))
total=sum(prices)
print(f"Products in stock: {stock}")
print(f"Total value: {total}")