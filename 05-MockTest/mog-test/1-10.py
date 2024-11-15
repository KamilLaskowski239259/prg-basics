def f(sentence):
    suma = 0
    for i in sentence:
        suma = suma + ord(i)
    
    if suma%3 == 0:
        return True
    else:
        return False
    
print(f("student"))