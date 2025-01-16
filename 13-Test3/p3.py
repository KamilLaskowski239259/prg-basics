def f(uid):
    unique_ids=[]
    for i in uid:
        if i in unique_ids:
            return False
        unique_ids.append(i)
    return True
        
print(f(["john5","ann123","JOHN5","xxx","abc333","a10"])) #should return true
print(f(["abc123","ann","abc123","a10"])) # False 
print(f(["bob2","bob2"])) # False 
print(f(["bob2","BOB2"])) # True