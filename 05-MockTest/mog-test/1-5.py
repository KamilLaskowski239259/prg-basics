def f(binary):
    is_binary=False
    for i in binary:
        if i=="0" or i=="1":
            is_binary = True
        else :
            is_binary = False
            break
    return is_binary
print(f('101'))
print(f('131'))