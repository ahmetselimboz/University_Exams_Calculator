import tkinter
from tkinter import *
from tkinter import messagebox

window = Tk()
M1 = StringVar()
M2 = StringVar()
M3 = StringVar()
window.configure(bg='#4663BE')
window.title("Harf Notu ve Ortalama Hesaplama")
window.geometry("400x300")
L3 = Label(text = "Vize-Final Notunuzu Giriniz", fg= "black", relief = RIDGE, height = 2, width=25, bg="#85F1FE")

L1 = Label(text = "Adı: ", bg="#21AEE4", font= "Calibri 10 bold")
L2 = Label(text = "Soyadı: ", bg="#21AEE4", font= "Calibri 10 bold")
V1 = Label(text = "Vize Notu: ", bg="#21AEE4", font= "Calibri 10 bold")
V2 = Label(text = "Final Notu: ", bg="#21AEE4", font= "Calibri 10 bold")

E2 = Entry(window, fg = "Black", bg="#8DBAFE")
E1 = Entry(window, fg = "Black", bg="#8DBAFE")
V3 = Entry(window, textvariable=M1, bg="#8DBAFE")
V4 = Entry(window, textvariable=M2, bg="#8DBAFE")

def cal_avg():
    F1 = int(V3.get())
    F2 = int(V4.get())
    value = ((F1*40)/100) + ((F2*60)/100)
    if value >= 70 :
        messagebox.showinfo(window,
                            message=E2.get() + " " + E1.get() + " " + "adlı öğrencinin\nHarf Notu: AA\nOrtalaması:" + " " + f"{value}")
    elif value < 70 and value >= 65:
        messagebox.showinfo(window,
                            message=E2.get() + " " + E1.get() + " " + "adlı öğrencinin\nHarf Notu: BA\nOrtalaması:" + " " + f"{value}")
    elif value < 65 and value >= 60:
        messagebox.showinfo(window,
                            message=E2.get() + " " + E1.get() + " " + "adlı öğrencinin\nHarf Notu: BB\nOrtalaması:" + " " + f"{value}")
    elif value < 60 and value >= 55:
        messagebox.showinfo(window,
                            message=E2.get() + " " + E1.get() + " " + "adlı öğrencinin\nHarf Notu: CB\nOrtalaması:" + " " + f"{value}")
    elif value < 55 and value >= 50:
        messagebox.showinfo(window,
                            message=E2.get() + " " + E1.get() + " " + "adlı öğrencinin\nHarf Notu: CC\nOrtalaması:" + " " + f"{value}")
    elif value < 50 and value >= 45:
        messagebox.showinfo(window,
                            message=E2.get() + " " + E1.get() + " " + "adlı öğrencinin\nHarf Notu: DC\nOrtalaması:" + " " + f"{value}")
    elif value < 45 and value >= 35:
        messagebox.showinfo(window,
                            message=E2.get() + " " + E1.get() + " " + "adlı öğrencinin\nHarf Notu: DD\nOrtalaması:" + " " + f"{value}")
    elif value < 35:
        messagebox.showinfo(window,
                            message=E2.get() + " " + E1.get() + " " + "adlı öğrencinin\nHarf Notu: FF\nOrtalaması:" + " " + f"{value}")

B1 = Button(window, text= "Result", command = cal_avg, height= 1, width=10, font= "Calibri 10 bold", bg="#85F1FE")

L1.place(relx = 0.1, rely=0.2)
L2.place(relx = 0.1, rely=0.3)
V1.place(relx = 0.1, rely=0.4)
V2.place(relx = 0.1, rely=0.5)
L3.place(relx = 0.13, rely=0.05)
E2.place(relx = 0.3 , rely = 0.2)
E1.place(relx = 0.3 , rely = 0.3)
V3.place(relx = 0.3, rely = 0.4)
V4.place(relx = 0.3, rely = 0.5)
B1.place(relx = 0.41, rely = 0.6)
window.mainloop()