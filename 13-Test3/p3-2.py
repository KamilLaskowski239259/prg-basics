def f(d):
    counter=0
    for i in d.values():
        if sum(d.values())/len(d) < i:
            counter+=1
    return counter

print(f({"LO231":150,"BA787":120,"NZ15":30})) #à 2 
print(f({"LO231":150,"BA787":20,"NZ15":30})) #à 1 

