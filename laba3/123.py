def split(lst, n):
    # Базовый случай: если n равно 1, возвращаем список как единственную часть
    if n == 1:
        return [lst]
    
    # Если количество частей больше длины списка, возвращаем список с пустыми частями
    if n > len(lst):
        return [lst[i:i+1] for i in range(len(lst))]

    # Рекурсивное деление списка
    result = [[] for _ in range(n)]
    for i, item in enumerate(lst):
        result[i % n].append(item)
    
    return result

# Примеры использования
print(split([1, 2, 3, 4, 5], 2))  
print(split([1, 2, 3, 4, 5], 3))  
