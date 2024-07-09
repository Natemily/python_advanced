n = int(input())
matrix = [[1 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i < j and i > n - 1 - j or i > j and i < n - 1 - j:
            matrix[i][j] = 0
for row in matrix:
    print(*row)