def encode_rsa(message):
    e, n = 17, 3233
    # Преобразуем сообщение в числовой формат с помощью ASCII-кодировки
    m = [ord(char) for char in message]

    # Шифруем сообщение с помощью открытого ключа
    c = [pow(char, e, n) for char in m]

    return c

def decode_rsa(message):
    d, n = 413, 3233
    # Расшифровываем сообщение с помощью закрытого ключа
    decrypted_message = [chr(pow(char, d, n)) for char in message]

    # Объединяем символы в строку
    return "".join(decrypted_message)


