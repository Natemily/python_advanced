n, m = [int(i) for i in input().split()]
matrix_1 = [[int(i) for i in input().split()] for _ in range(n)]
l = input()
matrix_2 = [[int(i) for i in input().split()] for _ in range(n)]
matrix = [[0] * m for _ in range(n)]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j] = matrix_1[i][j] + matrix_2[i][j]
    print(*matrix[i])