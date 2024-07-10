n = input()

def position(n):
    if n[0] == "a":
        return 1
    elif n[0] == "b":
        return 2
    elif n[0] == "c":
        return 3
    elif n[0] == "d":
        return 4
    elif n[0] == "e":
        return 5
    elif n[0] == "f":
        return 6
    elif n[0] == "g":
        return 7
    elif n[0] == "h":
        return 8

a = position(n) - 1
b = 8 - int(n[1])
for i in range(8):
    for j in range(8):
        if i == b and j == a:
            print("Q", end = " ")
        elif abs(i - b) == abs(j - a) or i == b or j == a:
            print("*", end = " ")
        else:
            print(".", end = " ")
    print()