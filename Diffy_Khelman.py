import random
from RGR import a

# Функция кодирования
def encode_Diffy(filename, password, a):
    encoded_text = ""
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    s = text
    a = int(a)
    global p, g, b

    # Задаем параметры протокола
    p = random.randint(1, 1000)  # простое число
    g = random.randint(1, 1000)  # основание

    # Сторона A генерирует свой приватный ключ

    # Сторона B генерирует свой приватный ключ
    b = random.randint(1, 999)
    # Сторона A вычисляет свой публичный ключ
    A_1 = pow(g, a)
    A = A_1 % p

    # Сторона B вычисляет свой публичный ключ
    B_1 = pow(g, b)
    B = B_1 % p

    # Обе стороны вычисляют общий секретный ключ
    kA_1 = pow(B, a)
    kA = kA_1 % p
    kB_1 = pow(A, b)
    kB = kB_1 % p

    # Проверяем, что общие секретные ключи совпадают
    if kA == kB:
        for i in range(len(s)):  # проходим по каждому символу строки
            c = chr(ord(s[i]) + kA)  # каждый символ сдвигаем на размер ключа
            s = s[:i] + c + s[i + 1:]

    else:
        print("Ошибка: секретные ключи не совпадают!")
    encoded_filename = "encoded_" + filename
    with open(encoded_filename, "w", encoding="utf-8") as file:
        file.write(password + "\n")
        file.write(s)
    print("Текст успешно закодирован и сохранен в файл", encoded_filename)

# Функция декодирования

def decode_Diffy(filename, password):
    decoded_text = ""
    with open(filename, "r", encoding="utf-8") as file:
        file_password = file.readline().strip()
        if password != file_password:
            print("Неверный пароль. Декодирование невозможно.")
            return
        encoded_text = file.read()
    s = encoded_text

    # Сторона A вычисляет свой публичный ключ
    A_1 = pow(g, int(a))
    A = A_1 % p

    # Сторона B вычисляет свой публичный ключ
    B_1 = pow(g, b)
    B = B_1 % p

    # Обе стороны вычисляют общий секретный ключ
    kA_1 = pow(B, int(a))
    kA = kA_1 % p
    kB_1 = pow(A, b)
    kB = kB_1 % p

    # Проверяем, что общие секретные ключи совпадают
    if kA == kB:
        for i in range(len(s)):  # проходим по каждому символу строки
            c = chr(ord(s[i]) - kA)  # каждый символ сдвигаем на размер ключа
            s = s[:i] + c + s[i + 1:]
    else:
        print("Ошибка: секретные ключи не совпадают!")
    decoded_filename = "decoded_" + filename[8:]
    with open(decoded_filename, "w", encoding="utf-8") as file:
        file.write(s)
    print("Текст успешно декодирован и сохранен в файл", decoded_filename)