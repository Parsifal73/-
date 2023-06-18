import random
from table import encode_table, decode_table
from Cezar import encode_Cezar_English, encode_Cezar_Russia, decode_Cezar_English, decode_Cezar_Russia
from Diffy_Khelman import encode_Diffy, decode_Diffy

# Функция ввода текста
def input_text():
    text = input("Введите текст: ")
    filename = input("Введите имя файла для сохранения: ")
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
    print("Текст сохранен в файл", filename)


# Функция печати файла на экране
def print_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()
    print(text)


# Основная программа
while True:
    print("="*30)
    print("Выберите действие:")
    print("1 - ввод текста и сохранение в файл")
    print("2 - кодирование текста")
    print("3 - декодирование текста")
    print("4 - печать файла на экране")
    print("5 - выход")

    choice = input("Ваш выбор (1-5): ")
    if choice == "1":
        input_text()

    elif choice == "2":
        filename = input("Введите имя файла для кодирования: ")
        password = input("Введите пароль для кодирования: ")
        print("Выберите способ кодиривония:")
        print("1 - табличное шифрование")
        print("2 - шифрование Цезаря")
        print("3 - шифрование Диффи-Хеллмана")
        method = input("Введите номер метода кодирования (1-3): ")
        if method == "1":
            encode_table(filename, password)
        if method == "2":
            global language
            shift = int(input("Введите количество сдвига: "))
            language = input("Укажите язык, на котором написано сообщение('Русский' или 'Английский'): ")
            if language == "Русский":
                encode_Cezar_Russia(filename, shift, password)
            elif language == "Английский":
                encode_Cezar_English(filename, shift, password)
        if method == "3":
            a = int(input("Введите публичный ключ: "))
            encode_Diffy(filename, password, a)

    elif choice == "3":
        filename = input("Введите имя файла для декодирования: ")
        password = input("Введите пароль для декодирования: ")
        method = input("Введите номер метода кодирования (1-3): ")
        if method == "1":
            decode_table(filename, password)
        if method == "2":
            # language = input("Какой язык вы выбирали? ")
            if language == "Русский":
                decode_Cezar_Russia(filename, password)
            if language == "Английский":
                decode_Cezar_English(filename, password)
        if method == "3":
            decode_Diffy(filename, password)

    elif choice == "4":
        filename = input("Введите имя файла для печати: ")
        print_file(filename)

    elif choice == "5":
        print("Выход.")
        break
    else:
        print("Неверный выбор. Попробуйте еще раз.")