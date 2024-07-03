from math import factorial
n, list_n = int(input()), []
for i in range(0, n+1):
     x = n - i
     list_n.append(int(factorial(n)/((factorial(i))*(factorial(x)))))
print(list_n)