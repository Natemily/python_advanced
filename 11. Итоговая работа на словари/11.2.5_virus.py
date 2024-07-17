p = [input() for i in range(int(input()))]
files = {i.split()[0]:i.split()[1:] for i in p}
ask = [input() for i in range(int(input()))]
dict = {'write': 'W', 'read': 'R','execute': 'X'}
for i in ask:
    a = i.split()
    if a[1] in files:
        if dict[a[0]] in files[a[1]]:
            print("OK")
        else:
            print("Access denied")