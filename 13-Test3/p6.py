def f(vname):
    if not (1<=len(vname)<=5):
        return False
    if not (vname[0].isalpha() or vname[0]=="_"):
        return False
    for i in vname[1:]:
        if not (i.isalnum() or i=="_"):
            return False
    return True

print(f("abc")) #à True 
print(f("Abc")) #à True 
print(f("aBC")) #à True 
print(f("_ab_c")) #à True 
print(f("abcdef")) #à False 
print(f("8abc")) #à False 
print(f("_aB8_")) #à True 
print(f("_4x")) #à True