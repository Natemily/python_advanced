def multiply_matrices(matrix1, matrix2):
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

n, m = [int(i) for i in input().split()]
matrix1 = []
for _ in range(n):
    matrix1.append(list(map(int, input().split())))
input()
m, k = [int(i) for i in input().split()]
matrix2 = []
for _ in range(m):
    matrix2.append(list(map(int, input().split())))

result = multiply_matrices(matrix1, matrix2)

for row in result:
    print(*row)