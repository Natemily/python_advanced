n = int(input())
matrix_1 = [[int(i) for i in input().split()] for _ in range(n)]
matrix_2 = [[matrix_1[j][i] for j in range(n)] for i in range(n)]
count = 0
for i in range(n):
    for j in range(1, n+1):
        if j in matrix_1[i] and j in matrix_2[i]:
            count += 1
if count == n**2:
    print("YES")
else:
    print("NO")