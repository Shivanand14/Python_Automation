#Assignment6

#brew install python-tk@3.9 . 
# // pip install pyperclip 
##curl https://files.pythonhosted.org/packages/a7/2c/4c64579f847bd5d539803c8b909e54ba087a79d01bb3aba433a95879a6c5/pyperclip-1.8.2.tar.gz > pyperclip.tar.gz

## tar -xzvf pyperclip.tar.gz
##cd pyperclip-1.8.2
##python3 setup.py install

#Pyperclip is a cross-platform Python module for copy and paste clipboard functions


import random
from tkinter import *
from tkinter import messagebox
import pyperclip

gui = Tk()
gui.title('Password Generator')
gui.geometry('250x200')
gui.resizable(0,0)

def process():
    length = int(string_pass.get())

    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    special = ['@', '#', '$', '%', '&', '*']
    all = lower + upper + num + special
    ran = random.sample(all,length)
    password = "".join(ran)
    messagebox.showinfo('Result', 'Your password {} \n\nPassword copied to clipboard'.format(password))
    pyperclip.copy(password)

string_pass = StringVar()
label = Label(text="Password Length").pack(pady=10)
txt = Entry(textvariable=string_pass).pack()
btn = Button(text="Generator", command=process).pack(pady=10)

gui.mainloop()