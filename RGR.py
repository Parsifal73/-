from tkinter import *


class Rgr():
    
    def __init__(self):
        self.root = Tk()
        self.f = Frame()
        self.b1 = Button(self.f, width = 21, height = 2, text = "Ввод и Сохранение файла", command = self.input_text)
        self.b2 = Button(self.f, width = 21, height = 2, text = "Кодирование текста", command = self.encode_text)
        self.b3 = Button(self.f, width = 21, height = 2, text = "Декодирование текста", command = self.decode_text)
        self.b4 = Button(self.f, width = 21, height = 2, text = "Вывод файла", command = self.print_file)

        self.canvas = Canvas(self.f, width = 120, height = 50)

        self.text1 = self.canvas.create_text(20, 20, text = "Слава АВТФ", font = ("Arial", 15))

        self.f.pack()
        self.canvas.pack()
        self.b1.pack()
        self.b2.pack()
        self.b3.pack()
        self.b4.pack()

        self.animate()

    def animate(self):
        self.canvas.move(self.text1, -5, 0)
        if self.canvas.coords(self.text1)[0] < -100:
            self.canvas.coords(self.text1, 200, 20)
        self.root.after(100, self.animate)

 

    # Функция ввода текста
    def input_text(self):
        self.f2 = Frame()
        self.l1 = Label(self.f2, width = 15, height = 2, text = "Ввведите текст")
        self.e1 = Entry(self.f2)
        self.l2 = Label(self.f2, width = 15, height = 2, text = "Ввведите имя файла")
        self.e2 = Entry(self.f2)
        self.b5 = Button(self.f2, width = 15, height = 2, text = "Сохранить", command = self.input_text_b)

        self.f2.pack()
        self.l1.pack()
        self.e1.pack()
        self.l2.pack()
        self.e2.pack()
        self.b5.pack()

        self.filename = self.e2.get()

        
    def input_text_b(self):
        with open(self.e2.get(), "w", encoding="utf-8") as self.file:
            self.file.write(self.e1.get())
        self.f2.destroy()

    # Функция кодирования
    def encode_text(self):
        self.f3 = Frame()
        self.l3 = Label(self.f3, width = 21, height = 2, text = "Ввведите секретное слово")
        self.e3 = Entry(self.f3)
        self.l4 = Label(self.f3, width = 15, height = 2, text = "Введите имя файла")
        self.e4 = Entry(self.f3)
        self.encoded_text = ""
        self.b6 = Button(self.f3, width = 15, height = 2, text = "Закодировать", command = self.encode_text_b)

        self.f3.pack()
        self.l3.pack()
        self.e3.pack()
        self.l4.pack()
        self.e4.pack()
        self.b6.pack()


    def encode_text_b(self):
        with open(self.e4.get(), "r", encoding="utf-8") as self.file:
            self.text = self.file.read()
            
        self.password = self.e3.get()
        
        for i in range(len(self.text)):
            self.nowChar = self.text[i]
            self.secretChar = self.password[i % len(self.password)]
            self.encoded_char = chr(ord(self.nowChar) + ord(self.secretChar))
            self.encoded_text += self.encoded_char
            
        self.encoded_filename = "encoded_" + self.e4.get()
        with open(self.encoded_filename, "w", encoding="utf-8") as self.file:
            self.file.write(self.password + "\n")
            self.file.write(self.encoded_text)
        self.f3.destroy()




    # Функция декодирования
    def decode_text(self):
        decoded_text = ""
        with open(filename, "r", encoding="utf-8") as file:
            file_password = file.readline().strip()
            if password != file_password:
                print("Неверный пароль. Декодирование невозможно.")
                return
            encoded_text = file.read()
        for i in range(len(encoded_text)):
            if encoded_text[i].isalnum():
                nowChar = encoded_text[i]
                secretChar = password[i % len(password)]
                decoded_char = chr(ord(nowChar) - ord(secretChar))
                decoded_text += decoded_char
            else:
                decoded_text += encoded_text[i]
        decoded_filename = "decoded_" + filename[8:]
        with open(decoded_filename, "w", encoding="utf-8") as file:
            file.write(decoded_text)
        print("Текст успешно декодирован и сохранен в файл", decoded_filename)

    # Функция печати файла на экране
    def print_file(self):
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
        print(text)

x = Rgr()
x.root.mainloop()
