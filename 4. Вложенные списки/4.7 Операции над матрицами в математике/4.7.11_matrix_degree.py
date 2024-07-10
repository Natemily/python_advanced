import numpy as np # type: ignore
def matrix_power(matrix, power):
    result = np.identity(len(matrix))
    for _ in range(power):
        result = np.dot(result, matrix)
    return result
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
m = int(input())
matrix_res = matrix_power(matrix, m)
result = [[0] * n for _ in range(n)]
for i in range(len(matrix_res)):
    for j in range(len(matrix_res[i])):
        result[i][j] = int(matrix_res[i][j])
    print(*result[i])