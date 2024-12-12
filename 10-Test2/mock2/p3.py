def f(array2D):
    for row in array2D:
        row_sum = sum(row)
    for j in range(len(array2D[0])):
        column_sum = sum(array2D[i][j] for i in range(len(array2D)))
    return row_sum == column_sum




print(f([[3,7,2],[4,2,5],[9,2,1]]))