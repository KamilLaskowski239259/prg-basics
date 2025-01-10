ms_to_kmh=lambda x: x*3.6
x=int(input("Enter m/s: "))
result=ms_to_kmh(x)
print(f"{x} m/s is {result}km/h")