car_speed = int(input("Enter your speed: "))
speed_min = 40
speed_max = 140
if car_speed < speed_min:
    print("Warning: invalid car speed!!! ")
elif car_speed > speed_max:
    print("Warning: invalid car speed!!! ")
else:
    print("Your speed is good")