line_1 = sorted("".join(input().replace('.', '').replace(',', '').replace('!', '').replace('?', '').replace(':', '').replace(';', '').replace('-', '').lower().split()))
line_2 = sorted("".join(input().replace('.', '').replace(',', '').replace('!', '').replace('?', '').replace(':', '').replace(';', '').replace('-', '').lower().split()))
res = "YES"
if line_1 != line_2:
        res = "NO"
print(res)