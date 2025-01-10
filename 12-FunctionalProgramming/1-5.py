def avg_speed(distance,hours,minutes):
    time=y+z/60
    speed=x/time
    return speed
x=int(input("Enter distance in km: "))
y=int(input("Enter number of travel hours: "))
z=int(input("Enter number of travel minutes: "))
result=avg_speed(x,y,z)
round_result=round(result, 1)
print(f"Average speed: {round_result} km/h")