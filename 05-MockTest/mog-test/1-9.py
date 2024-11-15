def f(sentance):
    sum=0
    for i in sentance:
        if i == 'a' or i== 'e' or i== 'i' or i== 'o' or i== 'u' or i=='y':
            sum+=1
    return sum
print(f("water"))
    
