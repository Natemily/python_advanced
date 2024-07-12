dict1 = {i.strip().lower(): j.strip() for i, j in (input().split(":") for _ in range(int(input())))}
dict2 = (input().lower() for _ in range(int(input())))
answers = []
for i in dict2:
    if i in dict1:
        answers.append(dict1[i])
    else:
        answers.append("Не найдено")
print(*answers, sep="\n")