def f(n):
    n_str=str(n)
    odd=[]
    for i in n_str:
        if int(i)%2==1:
            odd+=i   
    if odd==[]:
        return -1
    else:
        int_odd=[]
        for z in odd:
            int_odd.append(int(z))
        return max(int_odd)-min(int_odd)


print(f(10852)) #à 4 
print(f(723597)) #à 6 
print(f(4388)) #à 0 
print(f(846206)) #à -1 
