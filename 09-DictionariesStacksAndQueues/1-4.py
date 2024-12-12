person = {
   "name": "Kamil",
   "surname": "Laskowski",
   "age": 19,
   "hobby": ["FPV","sleeping"],
   "married": False,
   "phone":{"mobile":"603249392"}
}
print(person["name"])
print(person["hobby"])
for i,ii in person.items():
    print(f"{i}:{ii}")
person["surname"]="Nowak"
#print(person["surname"])
person["married"]=True
#print(person["married"])
person["gender"]='Male'
#print(person["gender"])
person["hobby"].append('bicycle')
#print(person["hobby"])
person["phone"]={"mobile":"603249392",'work':'793465872654'}
print("--------------------------")
print(person["phone"])
for i,ii in person.items():
    print(f"{i}:{ii}")