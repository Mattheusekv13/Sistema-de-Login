from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#Criar Janela
jan = Tk()
jan.title("DP System - Acess Panel")
jan.geometry("1200x600")
jan.configure(background="white")
jan.resizable(width=False, height=False)

#imagens
logo = PhotoImage(file="icon/logo.png")

#Widgets
LetFrame = Frame(jan, width=400, height=600, bg="MIDNIGHTBLUE", relief="raise")
LetFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=790, height= 600, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LetFrame, image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=100, y=100)

#Username
UserLabel = Label(RightFrame, text="Username:", font=("Arial", 20), bg="MIDNIGHTBLUE", fg="White")
UserLabel.place(x =20, y=200)

UserEntry = ttk.Entry(RightFrame, width=60)
UserEntry.place(x=300, y=220)

#Password
PassLabel = Label(RightFrame, text="Password:", font=("Arial", 20), bg="MIDNIGHTBLUE", fg="White")
PassLabel.place(x =20, y=400)

PassEntry = ttk.Entry(RightFrame, width=60)
PassEntry.place(x=300, y=420)

jan.mainloop()