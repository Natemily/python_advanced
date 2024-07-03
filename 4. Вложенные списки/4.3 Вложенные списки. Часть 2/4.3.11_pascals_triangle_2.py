from math import factorial
n = int(input())
for i in range(n):
    list_n = []
    for j in range(i+1):
        x = i - j
        list_n.append(int(factorial(i)/(factorial(j)*factorial(x))))
    print(*list_n)