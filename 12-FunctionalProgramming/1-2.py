# takes two numbers from keyboard
n1 = float(input("Enter x:"))
n2 = float(input("Enter y:"))

# define an anonymous function
mean = lambda x,y: (x+y)/2


# calculates arightmtic mean and print result
result = mean(n1,n2)
print(f"The arithmetic mean of {n1} and {n2} is {result}")