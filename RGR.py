from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as mb
from shamir import encrypt, decrypt
from RSA import encode_rsa, decode_rsa
from skitala import coding_skitala
from table import encode_table, decode_table
from Cezar import encode_Cezar_English, encode_Cezar_Russia, decode_Cezar_English, decode_Cezar_Russia
from Diffy_Khelman import encode_Diffy, decode_Diffy



class Rgr():

    def __init__(self):
        self.root = Tk()
        self.f = Frame()
        self.b1 = Button(self.f, width = 21, height = 2, text = "Ввод и Сохранение файла", command = self.input_text)
        self.b2 = Button(self.f, width = 21, height = 2, text = "Кодирование текста", command = self.encode)
        self.b3 = Button(self.f, width = 21, height = 2, text = "Декодирование текста", command = self.decode)

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
        self.l = Label(self.f2, width = 21, height = 2, text = "Ввведите секретное слово")
        self.e = Entry(self.f2)
        self.l1 = Label(self.f2, width = 15, height = 2, text = "Ввведите текст")
        
        self.text = Text(self.f2, width = 20, height = 7)
 
        self.scroll = Scrollbar(self.f2, command = self.text.yview)
 
        self.text.config(yscrollcommand = self.scroll.set)
        
        self.l2 = Label(self.f2, width = 15, height = 2, text = "Ввведите имя файла")
        self.e2 = Entry(self.f2)
        self.b5 = Button(self.f2, width = 15, height = 2, text = "Сохранить", command = self.input_text_b)

        self.f2.pack()
        self.l.pack()
        self.e.pack()
        self.l2.pack()
        self.e2.pack()
        self.l1.pack()
        self.text.pack()
        self.scroll.pack(side = LEFT, fill = Y)
        self.b5.pack(side = BOTTOM)

        self.filename = self.e2.get()

    def input_text_b(self):
        with open(self.e2.get(), "w", encoding="utf-8") as self.file:
            self.file.write(self.e.get() + "\n")
            self.file.write(self.text.get(1.0, END))
        self.f2.destroy()

    def encode(self):  
        self.f3 = Frame()
        self.l3 = Label(self.f3, width = 21, height = 2, text = "Ввведите секретное слово")
        self.e3 = Entry(self.f3)
        self.l4 = Label(self.f3, width = 15, height = 2, text = "Введите имя файла")
        self.e4 = Entry(self.f3)
        self.b6 = Button(self.f3, width = 15, height = 2, text = "Шамир", command = self.shamir_encode_text_b)
        self.b10 = Button(self.f3, width = 15, height = 2, text = "RSA", command = self.RSA_encode_text_b)
        self.b11 = Button(self.f3, width = 15, height = 2, text = "Скитала", command = self.skitala_encode_text_b)
        self.b12 = Button(self.f3, width = 15, height = 2, text = "Табличная", command = self.table_encode_text_b)
        self.b13 = Button(self.f3, width = 15, height = 2, text = "Цезарь", command = self.Cezar_encode_text_b)
        self.b14 = Button(self.f3, width = 15, height = 2, text = "Диффи хэллман", command = self.Diffy_encode_text_b)

        

        self.f3.pack()
        self.l3.pack()
        self.e3.pack()
        self.l4.pack()
        self.e4.pack()
        self.b6.pack()
        self.b10.pack()
        self.b11.pack()
        self.b12.pack()
        self.b13.pack()
        self.b14.pack()


    def shamir_encode_text_b(self):
        with open(self.e4.get(), "r", encoding="utf-8") as self.file:
            self.file_password = self.file.readline().strip()
            if self.e3.get() != self.file_password:
                mb.showerror("Error", "retard")
            else:
                mb.showinfo(":)", "Text successfully encoded")
                self.text = self.file.read()

        self.x = encrypt(self.text)

        self.encoded_filename = "encoded_shamir_" + self.e4.get()

        with open(self.encoded_filename, "w", encoding="utf-8") as self.file:
            self.file.write(self.file_password + "\n")
            for i in self.x:
                self.file.write('%s\n' % i)

        self.f3.destroy()
        

    def RSA_encode_text_b(self):
        with open(self.e4.get(), "r", encoding="utf-8") as self.file:
            self.file_password = self.file.readline().strip()
            if self.e3.get() != self.file_password:
                mb.showerror("Error", "retard")
            else:
                mb.showinfo(":)", "Text successfully encoded")
                self.text = self.file.read()

        self.x = encode_rsa(self.text)

        self.encoded_filename = "encoded_RSA_" + self.e4.get()

        with open(self.encoded_filename, "w", encoding="utf-8") as self.file:
            self.file.write(self.file_password + "\n")
            for i in self.x:
                self.file.write('%s\n' % i)
        
        self.f3.destroy()
        

    def skitala_encode_text_b(self):
        self.m = 3
        with open(self.e4.get(), "r", encoding="utf-8") as self.file:
            self.file_password = self.file.readline().strip()
            if self.e3.get() != self.file_password:
                mb.showerror("Error", "retard")
            else:
                mb.showinfo(":)", "Text successfully encoded")
                self.text = self.file.read()

        self.x = coding_skitala(self.text, self.m)

        self.encoded_filename = "encoded_skitala_" + self.e4.get()

        with open(self.encoded_filename, "w", encoding="utf-8") as self.file:
            self.file.write(self.file_password + "\n")
            self.file.write(self.x)

        
        self.f3.destroy()

    def table_encode_text_b(self):
        with open(self.e4.get(), "r", encoding="utf-8") as self.file:
            self.file_password = self.file.readline().strip()
            if self.e3.get() != self.file_password:
                mb.showerror("Error", "retard")
            else:
                mb.showinfo(":)", "Text successfully encoded")
                self.text = self.file.read()

        self.x = encode_table(self.text)

        self.encoded_filename = "encoded_table_" + self.e4.get()

        with open(self.encoded_filename, "w", encoding="utf-8") as self.file:
            self.file.write(self.file_password + "\n")
            self.file.write(self.x)

        
        self.f3.destroy()

    def Cezar_encode_text_b(self):
        with open(self.e4.get(), "r", encoding="utf-8") as self.file:
            self.file_password = self.file.readline().strip()
            if self.e3.get() != self.file_password:
                mb.showerror("Error", "retard")
            else:
                self.file_name = self.e4.get()
                self.f5 = Frame()
                self.l10 = Label(self.f5, width = 21, height = 2, text = "Ввведите смещение")
                self.e10 = Entry(self.f5)
                self.b20 = Button(self.f5, width = 15, height = 2, text = "Английский", command = self.Cezar_english_encode_text_b)
                self.b21 = Button(self.f5, width = 15, height = 2, text = "Русский", command = self.Cezar_russian_encode_text_b)

                self.f5.pack()
                self.l10.pack()
                self.e10.pack()
                self.b20.pack()
                self.b21.pack()

                self.f3.destroy()

    def Cezar_english_encode_text_b(self):
        with open(self.file_name, "r", encoding="utf-8") as self.file:
            self.file_password = self.file.readline().strip()
            self.text = self.file.read()

        self.x = encode_Cezar_English(self.text, self.e10.get())

        self.encoded_filename = "encoded_Cezar_" + self.file_name

        with open(self.encoded_filename, "w", encoding="utf-8") as self.file:
            self.file.write(self.file_password + "\n")
            self.file.write(self.x)

        self.f5.destroy()
        mb.showinfo(":)", "Text successfully encoded")

    def Cezar_russian_encode_text_b(self):
        with open(self.file_name, "r", encoding="utf-8") as self.file:
            self.file_password = self.file.readline().strip()
            self.text = self.file.read()

        self.x = encode_Cezar_Russia(self.text, self.e10.get())

        self.encoded_filename = "encoded_Cezar_" + self.file_name

        with open(self.encoded_filename, "w", encoding="utf-8") as self.file:
            self.file.write(self.file_password + "\n")
            self.file.write(self.x)

        self.f5.destroy()
        mb.showinfo(":)", "Text successfully encoded")

    def Diffy_encode_text_b(self):
        with open(self.e4.get(), "r", encoding="utf-8") as self.file:
            self.file_password = self.file.readline().strip()
            if self.e3.get() != self.file_password:
                mb.showerror("Error", "retard")
            else:
                mb.showinfo(":)", "Text successfully encoded")
                self.text = self.file.read()

        self.x = encode_Diffy(self.text)

        self.encoded_filename = "encoded_Diffy_" + self.e4.get()

        with open(self.encoded_filename, "w", encoding="utf-8") as self.file:
            self.file.write(self.file_password + "\n")
            self.file.write(self.x)

        
        self.f3.destroy()
        

    def decode(self):
        self.f4 = Frame()
        self.l5 = Label(self.f4, width = 21, height = 2, text = "Ввведите секретное слово")
        self.e5 = Entry(self.f4)
        self.l6 = Label(self.f4, width = 15, height = 2, text = "Введите имя файла")
        self.e6 = Entry(self.f4)
        self.b7 = Button(self.f4, width = 15, height = 2, text = "Шамир", command = self.shamir_decode_text_b)
        self.b15 = Button(self.f4, width = 15, height = 2, text = "RSA", command = self.RSA_decode_text_b)
        self.b16 = Button(self.f4, width = 15, height = 2, text = "Скитала", command = self.skitala_decode_text_b)
        self.b17 = Button(self.f4, width = 15, height = 2, text = "Табличная", command = self.table_decode_text_b)
        self.b18 = Button(self.f4, width = 15, height = 2, text = "Цезарь", command = self.Cezar_decode_text_b)
        self.b19 = Button(self.f4, width = 15, height = 2, text = "Диффи хэллман", command = self.Diffy_decode_text_b)

        self.f4.pack()
        self.l5.pack()
        self.e5.pack()
        self.l6.pack()
        self.e6.pack()
        self.b7.pack()
        self.b15.pack()
        self.b16.pack()
        self.b17.pack()
        self.b18.pack()
        self.b19.pack()



    def shamir_decode_text_b(self):
        self.decode = "encoded_shamir_" + self.e6.get()
        self.decode1 = self.e6.get()
        self.text_decode = list()
        with open(self.decode, "r", encoding = "utf-8") as self.file:
            self.file_password = self.file.readline().strip()
            if self.e5.get() != self.file_password:
                mb.showerror("Error", "retard")
            else:
                mb.showinfo(":)", "Text successfully decoded")
                for line in self.file:
                    currentPlace = line[:-1]
                    self.text_decode.append(int(currentPlace))

        print(self.text_decode)

        self.z = decrypt(self.text_decode)

            
        self.decoded_filename = "decoded_shamir_" + self.decode1
        with open(self.decoded_filename, "w", encoding="utf-8") as self.file:
            self.file.write(self.file_password + "\n")
            self.file.write(self.z)

        self.f4.destroy()

    def RSA_decode_text_b(self):
        self.decode = "encoded_RSA_" + self.e6.get()
        self.decode1 = self.e6.get()
        self.text_decode = list()
        with open(self.decode, "r", encoding = "utf-8") as self.file:
            self.file_password = self.file.readline().strip()
            if self.e5.get() != self.file_password:
                mb.showerror("Error", "retard")
            else:
                mb.showinfo(":)", "Text successfully decoded")
                for line in self.file:
                    currentPlace = line[:-1]
                    self.text_decode.append(int(currentPlace))

        print(self.text_decode)

        self.z = decode_rsa(self.text_decode)

            
        self.decoded_filename = "decoded_RSA_" + self.decode1
        with open(self.decoded_filename, "w", encoding="utf-8") as self.file:
            self.file.write(self.file_password + "\n")
            self.file.write(self.z)

        self.f4.destroy()

    def skitala_decode_text_b(self):
        self.m = 3
        self.decode = "encoded_skitala_" + self.e6.get()
        self.decode1 = self.e6.get()
        with open(self.decode, "r", encoding = "utf-8") as self.file:
            self.file_password = self.file.readline().strip()
            if self.e5.get() != self.file_password:
                mb.showerror("Error", "retard")
            else:
                mb.showinfo(":)", "Text successfully decoded")
                self.text = self.file.read()
                

        self.z = coding_skitala(self.text, self.m)

            
        self.decoded_filename = "decoded_skitala_" + self.decode1
        with open(self.decoded_filename, "w", encoding="utf-8") as self.file:
            self.file.write(self.file_password + "\n")
            self.file.write(self.z)

        self.f4.destroy()

    def table_decode_text_b(self):
        self.decode = "encoded_table_" + self.e6.get()
        self.decode1 = self.e6.get()
        with open(self.decode, "r", encoding = "utf-8") as self.file:
            self.file_password = self.file.readline().strip()
            if self.e5.get() != self.file_password:
                mb.showerror("Error", "retard")
            else:
                mb.showinfo(":)", "Text successfully decoded")
                self.text = self.file.read()
                

        self.z = decode_table(self.text)

            
        self.decoded_filename = "decoded_table_" + self.decode1
        with open(self.decoded_filename, "w", encoding="utf-8") as self.file:
            self.file.write(self.file_password + "\n")
            self.file.write(self.z)

        self.f4.destroy()


    def Cezar_decode_text_b(self):
        self.decode = "encoded_Cezar_" + self.e6.get()
        with open(self.decode, "r", encoding="utf-8") as self.file:
            self.file_password = self.file.readline().strip()
            if self.e5.get() != self.file_password:
                mb.showerror("Error", "retard")
            else:
                self.file_name = self.e6.get()
                self.f6 = Frame()
                self.l11 = Label(self.f6, width = 21, height = 2, text = "Ввведите смещение")
                self.e11 = Entry(self.f6)
                self.b22 = Button(self.f6, width = 15, height = 2, text = "Английский", command = self.Cezar_english_decode_text_b)
                self.b23 = Button(self.f6, width = 15, height = 2, text = "Русский", command = self.Cezar_russian_decode_text_b)

                self.f6.pack()
                self.l11.pack()
                self.e11.pack()
                self.b22.pack()
                self.b23.pack()

                self.f4.destroy()

    def Cezar_english_decode_text_b(self):
        self.decode = "encoded_Cezar_" + self.file_name
        with open(self.decode, "r", encoding="utf-8") as self.file:
            self.file_password = self.file.readline().strip()
            self.text = self.file.read()

        self.z = decode_Cezar_English(self.text, self.e11.get())

        self.decoded_filename = "decoded_Cezar_" + self.file_name

        with open(self.decoded_filename, "w", encoding="utf-8") as self.file:
            self.file.write(self.file_password + "\n")
            self.file.write(self.z)

        self.f6.destroy()
        mb.showinfo(":)", "Text successfully decoded")

    def Cezar_russian_decode_text_b(self):
        self.decode = "encoded_Cezar_" + self.file_name
        with open(self.decode, "r", encoding="utf-8") as self.file:
            self.file_password = self.file.readline().strip()
            self.text = self.file.read()

        self.z = decode_Cezar_Russia(self.text, self.e11.get())

        self.decoded_filename = "decoded_Cezar_" + self.file_name

        with open(self.decoded_filename, "w", encoding="utf-8") as self.file:
            self.file.write(self.file_password + "\n")
            self.file.write(self.z)

        self.f6.destroy()
        mb.showinfo(":)", "Text successfully decoded")

    def Diffy_decode_text_b(self):
        self.decode = "encoded_Diffy_" + self.e6.get()
        self.decode1 = self.e6.get()
        with open(self.decode, "r", encoding = "utf-8") as self.file:
            self.file_password = self.file.readline().strip()
            if self.e5.get() != self.file_password:
                mb.showerror("Error", "retard")
            else:
                mb.showinfo(":)", "Text successfully decoded")
                self.text = self.file.read()
                

        self.z = decode_Diffy(self.text)

            
        self.decoded_filename = "decoded_Diffy_" + self.decode1
        with open(self.decoded_filename, "w", encoding="utf-8") as self.file:
            self.file.write(self.file_password + "\n")
            self.file.write(self.z)

        self.f4.destroy()

x = Rgr()

x.root.mainloop()
