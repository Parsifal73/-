from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as mb
from shamir import encrypt, decrypt
from RSA import encode_rsa, decode_rsa



class Rgr():

    def __init__(self):
        self.root = Tk()
        self.f = Frame()
        self.b1 = Button(self.f, width = 21, height = 2, text = "Ввод и Сохранение файла", command = self.input_text)
        self.b2 = Button(self.f, width = 21, height = 2, text = "Кодирование текста", command = self.shamir_encode)
        self.b3 = Button(self.f, width = 21, height = 2, text = "Декодирование текста", command = self.shamir_decode)

        self.canvas = Canvas(self.f, width = 120, height = 50)

        self.text1 = self.canvas.create_text(20, 20, text = "Слава АВТФ", font = ("Arial", 15))

        self.f.pack()
        self.canvas.pack()
        self.b1.pack()
        self.b2.pack()
        self.b3.pack()

        self.animate()

    def animate(self):
        self.canvas.move(self.text1, -5, 0)
        if self.canvas.coords(self.text1)[0] < -100:
            self.canvas.coords(self.text1, 200, 20)
        self.root.after(100, self.animate)

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

    def shamir_encode(self):  
        self.f3 = Frame()
        self.l3 = Label(self.f3, width = 21, height = 2, text = "Ввведите секретное слово")
        self.e3 = Entry(self.f3)
        self.l4 = Label(self.f3, width = 15, height = 2, text = "Введите имя файла")
        self.e4 = Entry(self.f3)
        self.b6 = Button(self.f3, width = 15, height = 2, text = "Закодировать", command = self.shamir_encode_text_b)

        self.f3.pack()
        self.l3.pack()
        self.e3.pack()
        self.l4.pack()
        self.e4.pack()
        self.b6.pack()


    def shamir_encode_text_b(self):
        with open(self.e4.get(), "r", encoding="utf-8") as self.file:
            self.text = self.file.read()

        self.x = encrypt(self.text)

        self.encoded_filename = "encoded_" + self.e4.get()

        with open(self.encoded_filename, "w", encoding="utf-8") as self.file:
            for i in self.x:
                self.file.write('%s\n' % i)

        
        self.f3.destroy()

    def shamir_decode(self):
        self.f4 = Frame()
        self.l5 = Label(self.f4, width = 21, height = 2, text = "Ввведите секретное слово")
        self.e5 = Entry(self.f4)
        self.password = self.e5.get()
        self.l6 = Label(self.f4, width = 15, height = 2, text = "Введите имя файла")
        self.e6 = Entry(self.f4)
        self.encoded_text = ""
        self.b7 = Button(self.f4, width = 15, height = 2, text = "Декодировать", command = self.shamir_decode_text_b)

        self.f4.pack()
        self.l5.pack()
        self.e5.pack()
        self.l6.pack()
        self.e6.pack()
        self.b7.pack()


    def shamir_decode_text_b(self):
        self.decode = "encoded_" + self.e6.get()
        self.decode1 = self.e6.get()
        self.text_decode = list()
        with open(self.decode, "r", encoding = "utf-8") as self.file:
            for line in self.file:
                currentPlace = line[:-1]
                self.text_decode.append(int(currentPlace))

        print(self.text_decode)

        self.z = decrypt(self.text_decode)

            
        self.decoded_filename = "decoded_" + self.decode1
        with open(self.decoded_filename, "w", encoding="utf-8") as self.file:
            self.file.write(self.z)
        mb.showinfo(":)", "Text successfully decoded")



x = Rgr()

x.root.mainloop()
