class Square:
   def __init__(self, a):
      self.a = a
def area(self):
    return self.a * self.a
def parimeter(self):
    return self.a*4

square1 = Square(4)
square2 = Square(6)
square1.area=area(square1)
square1.parimeter=parimeter(square1)
square2.area=area(square2)
square2.parimeter=parimeter(square2)
print('Square with side 4:')
print(f'Area is {square1.area}',f'Perimeter is {square1.parimeter}')
print ('Square with side 6:')
print(f'Area is {square2.area}',f'Perimeter is {square2.parimeter}')