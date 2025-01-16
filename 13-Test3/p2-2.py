def f(x,y,d):
    d_str=str(d)

    count = 0
    for i in range(x,y+1):
        count=count+str(i).count(d_str)
    return count>0
print(f(10,15,"14")) #à True 
print(f(100,120,"11")) #à True 
print(f(205,210,"04")) #à False