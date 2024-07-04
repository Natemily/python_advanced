a, b, c = input().split(), input().split(), input().split()
st1, st2, st3 = {int(i) for i in a}, {int(i) for i in b}, {int(i) for i in c}
general12 = st1 & st2
general13 = st1 & st3
general23 = st3 & st2
general = general12 ^ general13 ^ general23 ^ st1 ^ st2 ^ st3
print(*sorted(general))