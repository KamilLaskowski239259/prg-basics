def f(x,y,digit):
    digit_str=str(digit)
    
    count=0
    for number in range(x,y+1):
        count=count+str(number).count(digit_str)
    return count

print(f(10,15,1)) #à 7 
print(f(28,32,2)) #à 3 
print(f(100,105,6)) #à 0 
print(f(100,101,0)) #à 	3
