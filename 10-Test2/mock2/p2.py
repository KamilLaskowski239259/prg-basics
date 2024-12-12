def f(arr):
    for num in arr:
        if arr.count(num) == 1:
            return num

print(f([7,7,5,7,7,7,7,7]))   

