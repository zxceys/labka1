# рекурсия
lst = [1, 2, 3, 4, 5]
n = 2
def split1(lst, n):
        if n == 0 or n == 1:
            return [lst]
        s = lst[::n]
        f = []
        for i in range(len(lst)):
            if i%n != 0:
                f.append(lst[i])
    
        
        return [s] +  split1(f, n-1)
        
    
s = split1(lst,n)
print(s)
s = split1(lst, 3)
print(s)
    





# итерация

def split2(lst, n):
    
    if n == 1:
        return [lst]
    
    
    if n > len(lst):
        return [lst[i:i+1] for i in range(len(lst))]

    
    result = [[] for _ in range(n)]
    for i, item in enumerate(lst):
        result[i % n].append(item)
    
    return result


print(split2([1, 2, 3, 4, 5], 2))  
print(split2([1, 2, 3, 4, 5], 3)) 
 