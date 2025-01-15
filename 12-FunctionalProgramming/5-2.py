from functools import reduce
numbers = [2,4,6,3,7,5]
even=list(filter(lambda x: x%2==0,numbers))
result=reduce(lambda x,y:x+y,even)
print(f"Sum of even numbers is {result}")