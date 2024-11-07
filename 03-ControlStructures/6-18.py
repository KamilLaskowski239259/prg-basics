x = int(input("X: "))
y = int(input("Y: "))
quadtar = " "

if x < 0 and y > 0:
    quadrat = "First"
elif x > 0 and y > 0:
    quadrat = "Second"
elif x > 0 and y < 0:
    quadrat = "Third"
elif x < 0 and y < 0:
    quadrat = "Fourth"
else:
    quadrat = "Somewhere in betwen"
print(f"Point P({x},{y} is in {quadrat} quadrat)")

