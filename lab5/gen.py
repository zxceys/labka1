import math
from functools import reduce
def pi():
    i = 0
    p = str(math.pi)
    while i < len(p):
        yield int(p[i])/(int(p[i])**2)
        i +=1 
        if i == 1:
            i+=1
f = pi()
for i in f:
    print(i)        
def sum(pi):
    g = list(pi())
    suma = reduce(lambda x,y: x+y, g)
    return suma
result = sum(pi)
print(f'Сумма значений равна:', result)


