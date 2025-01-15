temps = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
pos=list(filter(lambda city:temps[city]>0,temps))
print(f"Cities with positive temperatures: {pos}")