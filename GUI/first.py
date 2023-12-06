from tkinter import *

def clicked():
    lbl.configure(text="Button was clicked !!!")
janela = Tk()
janela.title("Welcome nerds")
janela.geometry('350x200')
lbl = Label(janela, text="Ola")
lbl.pack()

lblTwo = Label(janela, text="This is Label widget", fg="red", font=("Helvetica", 16))
lblTwo.place(x=60, y=50)
txtfld=Entry(janela, text="This is Entry Widget", bd=5)
txtfld.place(x=80, y=120)
btn = Button(janela, text="Clique aqui", command=clicked)

from tkinter.ttk import Combobox

data=("one", "two","three", "four")
cb=Combobox(janela, values=data)
cb.place(x=60, y=150)

data=("one", "two","three", "four")
lb=Listbox(janela, height=5, selectmode='multiple')
for num in data:
    lb.insert(END, num)
lb.place(x=250, y=150)

btn.pack()
janela.mainloop()