lines = [[i.lower() for i in input().split()] for _ in range(int(input()))]
ask = [input().lower() for _ in range(int(input()))]
matrix = {}
for i in range(len(lines)):
    key = lines[i][-1]
    value = lines[i][:-1]
    if key not in matrix:
        matrix[key] = value
    else:
        matrix[key] = matrix[key] + value
for i in ask:
    if i in matrix:
        print(*matrix[i])
    else:
        print('абонент не найден')

