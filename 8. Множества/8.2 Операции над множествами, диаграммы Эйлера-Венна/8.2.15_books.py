n, m, k, x, y, z ,t ,a = [int(input()) for _ in range(8)]
b = n+m-t-x
d = m+k-t-y
c = n+k-t-z
one_book = k + n + m - 3*t - 2*c - 2*b - 2*d
two_book= b + d + c
lodyri = a-(one_book + two_book + t)

print(one_book , two_book, lodyri, sep='\n')