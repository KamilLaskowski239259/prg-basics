###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = float(input('a= '))
b = float(input('b= '))
c = float(input('c= '))

volume = a * b * c
surface_area = 2 * (a * b + b * c + c * a)

print(f'The volume of a cuboid with sides {a}, {b}, {c} is {volume}')
print(f'The surface area of a cuboid with sides {a}, {b}, {c} is {surface_area}')
