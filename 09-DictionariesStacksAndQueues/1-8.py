price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}
for key,value in price_list.items():
    print(key,value)
total=0
for value in price_list.values():
    total=total+value
print("Total=",total)
for key,value in price_list.items():
    print(key,(value*0.9))
