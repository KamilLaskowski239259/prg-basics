def f(arr2D):
    column_sum=[0]*len(arr2D[0])
    for row in arr2D:
        for i in range(len(row)):
            column_sum[i]+=row[i]
    for i in range(len(column_sum)):
        for j in range(i + 1, len(column_sum)):
            if column_sum[i] == column_sum[j]:
                return True
    return False


print(f([[3,4,2],[5,1,6]])) #à True 
print(f([[3,4,2],[5,1,7]])) #à False 
print(f([[3,4],[5,1],[4,7]])) #à True 
print(f([[3,4],[5,9],[4,7]])) #à False 