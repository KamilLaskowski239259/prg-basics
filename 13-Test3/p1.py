def f(word):
    if not word:
        return ""
    
    wave=[]
    for i in range(len(word)):
        wave.append(word[:i].lower()+word[i].upper()+word[i+1:].lower())
    return "-".join(wave)

print(f("book"))
print(f("water"))
print(f("ok"))
print(f("a"))
print(f(""))