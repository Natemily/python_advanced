list, list_a = [], []
for i in input().split():
    if len(list_a) == 0:
        list_a.append(i)
    else:
        if list_a[-1] == i:
            list_a.append(i)
        else:
            list.append(list_a)
            list_a = []
            list_a.append(i)
if len(list_a) != 0:
    list.append(list_a)
print(list)