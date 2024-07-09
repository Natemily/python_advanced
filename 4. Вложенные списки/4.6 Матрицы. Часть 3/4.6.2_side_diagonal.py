import math
n = int(input())
matrix = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    matrix[i][n - i - 1] = 1

for i in range(n):
    for j in range(n):
        if i < j and i > n - 1 - j or i > j and i > n - 1 - j:
            matrix[i][j] = 2

if n % 2 == 0:
    k = n // 2
else:
    k = math.ceil(n / 2)
    
for i in range(k, n):
    matrix[i][i] = 2
        
for row in matrix:
    print(*row)