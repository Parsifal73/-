# Шифр Скитала (или шифр древней Спарты)
from math import ceil  # функция округления вверх
 
def coding_skitala(s, m):  
    k = len(s) # Длинна сообщения
    l = ceil(k / m)  # Количество столбцов
    a = [[' ' for _ in range(l)] for _ in range(m)]  # Матрица для заполнения
    
    ind = 0
    for i in range(m):  # Записываем текст в таблицу
        for j in range(l):
            a[i][j] = s[ind]
            ind += 1
            if ind >= k: break
    """
    print('Исходная таблица')
    for i in range(m):
        print(a[i])
    """
    # Шифрованный текст считывается по строкам справа-налево, сверху-вниз
    # В оригинале считывание по столбцам
    s1 = ''
    for i in range(m):  # Считываем текст в строку
        for j in reversed(range(l)):
            s1 += a[i][j]
 
    return s1
 
# - белХг умесв .аволо
#s = coding_skitala(' - белХг умесв .аволо', 3)
#print('\nРезультат:', s)
