import linecache

def encode_Cezar_English(filename, password, shift):
    encoded_text = ""
    with open(filename, "r", encoding="utf-8") as file:
        file_password = file.readline().strip()
        if password != file_password:
            print("Неверный пароль. Декодирование невозможно.")
            return
        text = file.read()
    # encrypted = []

    # shift = int(input("Введите количество сдвига: "))

    for c in text:
        if c.isupper():  # проверить, является ли символ прописным
            c_index = ord(c) - ord('A')
            # сдвиг текущего символа на позицию key
            c_shifted = (c_index + int(shift)) % 26 + ord('A')
            c_new = chr(c_shifted)
            encoded_text += c_new
        elif c.islower():  # проверка наличия символа в нижнем регистре
            # вычесть юникод 'a', чтобы получить индекс в диапазоне [0-25)
            c_index = ord(c) - ord('a')
            c_shifted = (c_index + int(shift)) % 26 + ord('a')
            c_new = chr(c_shifted)
            encoded_text += c_new
        elif c.isdigit():
            # если это число, сдвинуть его фактическое значение
            c_new = (int(c) + int(shift)) % 10
            encoded_text += str(c_new)
        else:
            # если нет ни алфавита, ни числа, оставьте все как есть
            encoded_text += c

    encoded_filename = "encoded_" + filename
    # объединяем список символов в зашифрованную строку
    # encrypted_message = ''.join(encrypted)
    with open(encoded_filename, "w", encoding="utf-8") as file:
        file.write(password + "\n")
        file.write(str(shift) + "\n")
        file.write(encoded_text)
    print("Текст успешно закодирован и сохранен в файл", encoded_filename)

def encode_Cezar_Russia(filename, password, shift):
    encoded_text = ""
    with open(filename, "r", encoding="utf-8") as file:
        file_password = file.readline().strip()
        if password != file_password:
            print("Неверный пароль. Декодирование невозможно.")
            return
        text = file.read()
    # encrypted = []

    # shift = int(input("Введите количество сдвига: "))

    for c in text:
        if c.isupper():  # проверить, является ли символ прописным
            c_index = ord(c) - ord('А')
            # сдвиг текущего символа на позицию key
            c_shifted = (c_index + int(shift)) % 33 + ord('А')
            c_new = chr(c_shifted)
            encoded_text += c_new
        elif c.islower():  # проверка наличия символа в нижнем регистре
            # вычесть юникод 'a', чтобы получить индекс в диапазоне [0-25)
            c_index = ord(c) - ord('а')
            c_shifted = (c_index + int(shift)) % 33 + ord('а')
            c_new = chr(c_shifted)
            encoded_text += c_new
        elif c.isdigit():
            # если это число, сдвинуть его фактическое значение
            c_new = (int(c) + int(shift)) % 10
            encoded_text += str(c_new)
        else:
            # если нет ни алфавита, ни числа, оставьте все как есть
            encoded_text += c

    encoded_filename = "encoded_" + filename
    # объединяем список символов в зашифрованную строку
    # encrypted_message = ''.join(encrypted)
    with open(encoded_filename, "w", encoding="utf-8") as file:
        file.write(password + "\n")
        file.write(str(shift) + "\n")
        file.write(encoded_text)
    print("Текст успешно закодирован и сохранен в файл", encoded_filename)

# Функция декодирования

def decode_Cezar_English(filename, password):
    decoded_message = ""
    with open(filename, "r", encoding="utf-8") as file:
        # file_password = file.readline().strip()
        file_password = linecache.getline(filename, 1)
        if password != file_password:
            print("Неверный пароль. Декодирование невозможно.")
            return
        shift = int(linecache.getline(filename, 2))
        encoded_text = file.read()
    # decoded_message = []

    # перебираем все символы в сообщении
    for c in encoded_text:
        if c.isupper():
            c_index = ord(c) - ord('A')
            # сдвинуть текущий символ влево на позицию клавиши, чтобы получить его исходное положение
            c_og_pos = (c_index - int(shift)) % 26 + ord('A')
            c_og = chr(c_og_pos)
            decoded_message += c_og
        elif c.islower():
            c_index = ord(c) - ord('a')
            c_og_pos = (c_index - int(shift)) % 26 + ord('a')
            c_og = chr(c_og_pos)
            decoded_message += c_og
        elif c.isdigit():
            # если это число, сдвиньте его фактическое значение
            c_og = (int(c) - int(shift)) % 10
            decoded_message += str(c_og)
        else:
            # если нет ни алфавита, ни числа, оставьте все как есть
            decoded_message += c

    # объединяем список символов в зашифрованную строку
    # decoded_message = ''.join(decoded_message)
    decoded_filename = "decoded_" + filename[8:]
    with open(decoded_filename, "w", encoding="utf-8") as file:
        file.write(decoded_message)
    print("Текст успешно декодирован и сохранен в файл", decoded_filename)

def decode_Cezar_Russia(filename, password):
    decoded_message = ""
    with open(filename, "r", encoding="utf-8") as file:
        # file_password = file.readline().strip()
        file_password = linecache.getline(filename, 1)
        if password != file_password:
            print("Неверный пароль. Декодирование невозможно.")
            return
        shift = int(linecache.getline(filename, 2))
        encoded_text = file.read()
    # decoded_message = []

    # перебираем все символы в сообщении
    for c in encoded_text:
        if c.isupper():
            c_index = ord(c) - ord('А')
            # сдвинуть текущий символ влево на позицию клавиши, чтобы получить его исходное положение
            c_og_pos = (c_index - int(shift)) % 33 + ord('А')
            c_og = chr(c_og_pos)
            decoded_message += c_og
        elif c.islower():
            c_index = ord(c) - ord('а')
            c_og_pos = (c_index - int(shift)) % 33 + ord('а')
            c_og = chr(c_og_pos)
            decoded_message += c_og
        elif c.isdigit():
            # если это число, сдвиньте его фактическое значение
            c_og = (int(c) - int(shift)) % 10
            decoded_message += str(c_og)
        else:
            # если нет ни алфавита, ни числа, оставьте все как есть
            decoded_message += c

    # объединяем список символов в зашифрованную строку
    # decoded_message = ''.join(decoded_message)
    decoded_filename = "decoded_" + filename[8:]
    with open(decoded_filename, "w", encoding="utf-8") as file:
        file.write(decoded_message)
    print("Текст успешно декодирован и сохранен в файл", decoded_filename)
