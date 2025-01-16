def f(mnumbers):
    counter=len(mnumbers)
    for x in mnumbers:
        for i in x:
            if i not in ["a","b","c","d","A","B","C","D","+","-","1","2","3","4","5","6","7"]:
                counter-=1
                break
    return counter
print(f(["A15","-31","7abC","+D1","-gH"])) #à 4 
print(f(["A05","-3+1","7ab8C","+D1","-22k"])) #à 1