k = input().split()
n, m = int(k[0]), int(k[1])
matrix = [[None] * m for _ in range(n)]
a = 0
for i in range(n):
    for j in range(m):
        matrix[i][j] = a + 1
        if a + 1 >= m:
            a = 0
        else:
            a += 1
    if a + 1 >= m:
        a = 0
    else:
        a = matrix[i][0]
for row in matrix:
    print(*row)