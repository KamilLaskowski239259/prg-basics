dog_age=int(input("Enter dog's age: "))
while dog_age<=2:
    human_age=dog_age*10.5
    break
else:
    human_age=((dog_age-2)*4)+21
print(f'Dog is {human_age} human years old')