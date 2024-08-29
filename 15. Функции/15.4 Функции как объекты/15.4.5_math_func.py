import math
def square(x):
    return x**2

def cube(x):
    return x**3

def root(x):
    return x**0.5

def fabs(x):
    return math.fabs(x)

def sin(x):
    return math.sin(x)


commands = {'квадрат': square, 'куб': cube, 'корень': root, 'модуль': fabs, 'синус': sin}

x = int(input())
command = input()

print(commands[command](x))