###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
import math
def triangle_area(a,b,c):
    s=(a+b+c)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area
a=int(input('A: '))
b=int(input('B: '))
c=int(input('C: '))
sum_value=triangle_area(a, b, c)
print(f'The area of a triangle with sides {a},{b},{c} is {sum_value}')

