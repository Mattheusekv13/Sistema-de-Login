from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#Criar Janela
jan = Tk()
jan.title("Eduardo's System - Painel de Acesso")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.attributes("-alpha",0.9)
#jan.iconbitmap(default="icon/LogoIcon.ico")

#imagens
logo = PhotoImage(file="icon/logo.png")

#Widgets
LetFrame = Frame(jan, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
LetFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height= 300, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LetFrame, image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=50, y=50)

#Username
UserLabel = Label(RightFrame, text="Nome:", font=("Arial", 20), bg="MIDNIGHTBLUE", fg="White")
UserLabel.place(x =25, y=80)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=150, y=90)

#Password
PassLabel = Label(RightFrame, text="Senha:", font=("Arial", 20), bg="MIDNIGHTBLUE", fg="White")
PassLabel.place(x =25, y=140)

PassEntry = ttk.Entry(RightFrame, width=30, show="*")
PassEntry.place(x=150, y=150) 

LoginButton = ttk.Button(RightFrame, text="Login", width=30)
LoginButton.place(x=100, y=225)

def Register():
    LoginButton.place(x=500000)

RegisterButton = ttk.Button(RightFrame, text="Register", width=20, command=Register)
RegisterButton.place(x=125, y=260)

jan.mainloop()