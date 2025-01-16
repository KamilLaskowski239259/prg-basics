def f(uid):
    for i in uid:
        if uid[:i]==uid[i]:
            return False
        else:
            return True
        
print(f(["john5","ann123","JOHN5","xxx","abc333","a10"])) #should return true
