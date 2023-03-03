from mimetypes import init
from tkinter import *

def login():

    uname=username.get()
    pwd=password.get()

    if uname=='' or pwd=='':
        message.set("fill the empty field!!!")
    else:
        if uname=="abcd@gmail.com" and pwd=="abc123":
            message.set("Login success")
            nextPage()

        else:
            message.set("Wrong username or password!!!")

def nextPage():
    login_screen.destroy()
    import init

def Loginform():
    global login_screen
    login_screen = Tk()
    
    login_screen.title("Login Form")
    
    login_screen.geometry("300x250")
    
    global  message
    global username
    global password
    username = StringVar()
    password = StringVar()
    message=StringVar()
    
    Label(login_screen,width="300", text="Please enter details below", bg="orange",fg="white").pack()
    
    Label(login_screen, text="Username * ").place(x=20,y=40)
    
    Entry(login_screen, textvariable=username).place(x=90,y=42)
    
    Label(login_screen, text="Password * ").place(x=20,y=80)
    
    Entry(login_screen, textvariable=password ,show="*").place(x=90,y=82)
    
    Label(login_screen, text="",textvariable=message).place(x=95,y=100)
    
    Button(login_screen, text="Login", width=10, height=1, bg="orange",command=login).place(x=105,y=130)
    login_screen.mainloop()
Loginform()