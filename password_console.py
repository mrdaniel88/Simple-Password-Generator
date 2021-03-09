# -*- coding: utf-8 -*-

from tkinter import *
import password_generator as pg

# top = Tk()


# var = StringVar()
# pass_length = StringVar()
# #pass_length_str = str(pass_length.set(pg.generate_password(pass_length)))
# label = Message(top, textvariable = var)


# var.set("Type your password length: ")
# label.pack()
# L1 = Label(top, text="Length: ")
# L1.pack( side = LEFT)
# E1 = Entry(top, bd =5, textvariable = pass_length_str)
# E1.pack(side = RIGHT)

# top.mainloop()

def password_console() -> None:
    password_length = int(input("Type your password length: "))
    password = pg.generate_password(password_length)
    print("Your password is: ", password)
    
password_console()