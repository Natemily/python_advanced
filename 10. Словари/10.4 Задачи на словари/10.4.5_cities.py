lines = [[i for i in input().split()] for _ in range(int(input()))]
ask = [input() for _ in range(int(input()))]
matrix = {}
for i in range(len(lines)):
    key = lines[i][0]
    value = lines[i][1:]
    if key not in matrix:
        matrix[key] = value
    else:
        matrix[key] = matrix[key] + value
for i in ask:
    for k, v in matrix.items():
        if i in v:
            print(k)
