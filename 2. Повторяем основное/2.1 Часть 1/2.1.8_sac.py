n = input()
k = len(n)-1
m = []
if len(n) % 3 == 1:
    m.append(n[0])
    k = 1
elif len(n) % 3 == 2:
    m.append(n[0 : 2])
    k = 2
elif len(n) <= 3:
    m.append(n)
elif len(n) % 3 == 0:
    m.append(n[0 : 3])
    k = 3
    
if len(n) >= 4:
    while k < len(n):
        m.append("," + n[k:k+3])
        k += 3
        
print(*m, sep="")