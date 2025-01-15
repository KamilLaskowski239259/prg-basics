names = [
   'James',
   'Emily',
   'William',
   'Olivia',
   'Benjamin',
   'Sophia',
   'Henry']
sorted_list=lambda names: sorted(names,key=len)

result=sorted_list(names)
print("Sorted list:")
for name in result:
    print(name)

    