def f(d):
    inside=[]
    for entry in d:
        reg_num,key=entry
        if key=="in":
            if reg_num not in inside:
                inside.append(reg_num)
        elif key=="out":
            if reg_num in d:
                inside.remove(reg_num)
    return sorted(inside)
cars = [["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"], ["BA111","in"],["BA123","out"],["KR234","in"]]
print(f(cars))
cars1 = [["KR234","in"],["KR234","out"]]
print(f(cars1))






