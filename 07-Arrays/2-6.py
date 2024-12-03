matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

def diagonal(matrix):
    for i in range(len(matrix)):
        matrix[i][i] = 1 
    return matrix

result = diagonal(matrix)

for row in result:
    print("".join(map(str, row)))  