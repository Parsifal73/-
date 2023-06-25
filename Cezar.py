def encode_Cezar_English(message, shift):
    
    encoded_text = ""

    for c in message:
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
            
    return encoded_text

def encode_Cezar_Russia(message, shift):
    encoded_text = ""
    
    for c in message:
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

    return encoded_text

# Функция декодирования

def decode_Cezar_English(encoded_text, shift):
    decoded_message = ""

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

    return decoded_message

def decode_Cezar_Russia(encoded_text, shift):
    decoded_message = ""

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

    return decoded_message
