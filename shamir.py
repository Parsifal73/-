# Шаг 1: Шифрование сообщения
def encrypt(message):
    public_key = 17, 3233
    e, n = public_key
    encrypted_message = []
    for char in message:
        m = ord(char)
        c = pow(m, e, n)
        encrypted_message.append(c)
    return encrypted_message

# Шаг 2: Расшифрование сообщения

def decrypt(message):
    private_key = 413, 3233
    d, n = private_key
    decrypted_message = ""
    for c in message:
        m = pow(c, d, n)
        char = chr(m)
        decrypted_message += char
    return decrypted_message
