storage={
'Laptop': 15,
'Desktop PC': 10,
'Monitor': 25,
'Keyboard': 50,
'Mouse': 60,
'External Hard Drive': 30,
'Printer': 12,
'Router': 20,
'USB Flash Drive': 100,
'Graphics Card': 8
}
for key,value in storage.items():
    print(key,value)
total=0
for value in storage.values():
    total=total+value
print("Total=",total)