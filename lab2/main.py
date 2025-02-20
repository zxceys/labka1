# Задача 1
import itertools
s = 'ГЕПАРД'
f = 0

for x in itertools.product(s, repeat=5):
    if x.count('Г') == 1 and x[0] != 'А' and x[4] != 'Е':
        f += 1 
print('Задача 1: ответ', f)
    
# Задача 2
s = 5**36 + 5**24 - 25
r = ''
while s != 0:
    r+= str(s%5)
    s//= 5
print('Задача 2: ответ', r.count('4'))

# Задча 3
print('Задача 3:')
c = 0
for i in range(500000, 600000):
    for d in range(18, (i//2 +1)):
        if ((i% d) == 0) and ((d % 10)== 8):
            c +=1
            print(i, d)
            break
    if c == 5:
        break
