###
# The program calculates the cost of transporting goods
# based on the given distance in km, fuel price per 1 liter,
# and fuel consumption in liters per 100 km.
#
distance = int(input('Enter distance in km: '))
fuel_price = float(input('Enter fuel price per liter: '))
fuel_consumption = float(input('Enter fuel consumption in L/KM: '))
total_fuel_consumption = round(distance/fuel_consumption, 2)
total_cost = round(total_fuel_consumption*fuel_price, 2)
print(f"You used {total_fuel_consumption} liter of fuel")
print(f"You have to pay {total_cost}")