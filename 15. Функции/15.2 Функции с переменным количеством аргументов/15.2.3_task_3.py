def mean(*elem):
    a = 0
    sum = 0
    res = 0
    for i in elem:
        if type(i) is int or type(i) is float:
            a += 1
            sum += i
    if sum == 0 and a == 0:
        res = 0
    else:
        res = sum /a 
    return res