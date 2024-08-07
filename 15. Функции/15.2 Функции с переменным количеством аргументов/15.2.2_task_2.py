def sq_sum(*args):
    sum = 0
    for i in range(len(args)):
        sum += args[i]**2
    return sum