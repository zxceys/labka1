#рекурсия
def v(i):
    if i == 1:
        return 0
    if i == 2:
        return 0
    if i == 3:
        return 1.5
    else:
        return ((i + 1)/(i**2 + 1)) * v(i-1) - (v(i-2) * v(i-3))
print(v(7))




#итерация
def f(n):
    if n == 1 or n == 2:
        return 0
    elif n == 3:
        return 1.5
    
    v = [0] * (n + 1)  
    v[1] = 0
    v[2] = 0
    v[3] = 1.5
    
    for i in range(4, n + 1):
        v[i] = (i + 1) / (i**2 + 1) * v[i - 1] - v[i - 2] * v[i - 3]
    
    return v[7]
print(f(7))



