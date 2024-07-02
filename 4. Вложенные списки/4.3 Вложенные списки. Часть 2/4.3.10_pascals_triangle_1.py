n, list_n = int(input()), []
k = 0
while 0 >= k < 2:
    list_n.append(1)
    k -= 1
for i in range(2, n//2+1):
    x = n - i
    list_n.append(((n-1)*n)/(((i-1)*i)*((x-1)*x)))
print(list_n)