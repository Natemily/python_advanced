friges = [input() for i in range(int(input()))]
a = "anton"
for i in range(len(friges)):
    j = 0
    k = 0
    count = 0
    while j < len(friges[i]) and k < len(a):
        if friges[i][j] == a[k]:
            count += 1
            k += 1
        j += 1
    if count == len(a):
        print(i+1, end = " ")