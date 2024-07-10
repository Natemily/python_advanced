matrix = [[int(i) for i in input().split()] for _ in range(int(input()))]
res = "YES"
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] != matrix[len(matrix)-j-1][len(matrix)-i-1]:
            res = "NO"
            break
print(res)