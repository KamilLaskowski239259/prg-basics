def f(n1,n2,n3):
    if n1==n2 or n1==n3 or n2==n3:
        result=False
    else:
        result=True
    return result
n1=int(input("Enter n1: "))
n2=int(input("Enter n2: "))
n3=int(input("Enter n3: "))
x=f(n1,n2,n3)
print(f"({n1},{n2},{n3} returns {x})")