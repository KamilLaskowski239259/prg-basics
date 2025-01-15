data=[("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
   ("Jackson","Peter"),("Johnson","Rick"),
   ("Lewis","Terry"),("Clarke","Robin")]
result=list(map(lambda item: item[0].upper()+', '+item[1],data))
for name in result:
    print(name)