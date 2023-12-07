from tkinter import *
from tkinter.ttk import Combobox

def clicked():
    lbl.configure(text="Button was clicked !!!")
janela = Tk()
janela.title("Welcome nerds")
janela.geometry('350x500')
lbl = Label(janela, text="Ola")
lbl.pack()

lblTwo = Label(janela, text="This is Label widget", fg="red", font=("Helvetica", 16))
lblTwo.place(x=100, y=50)

# Entrada de texto

def perdeuFoco(teste):
    lbl3 =  Label(janela, text="Saiu", fg="red", font=("Helvetica", 16))
    lbl3.place(x=80, y=180)
txtfld=Entry(janela, text="This is Entry Widget", bd=5)
txtfld.place(x=80, y=120)
txtfld.bind('<FocusOut>', perdeuFoco)

btn = Button(janela, text="Clique aqui", command=clicked)

#Combobox
data=("one", "two","three", "four")
cb=Combobox(janela, values=data)
cb.place(x=60, y=150)

# Listbox
data=("one", "two","three", "four")
lb=Listbox(janela, height=5, selectmode='multiple')
for num in data:
    lb.insert(END, num)
lb.place(x=50, y=400)

#Radiobutton
v0=IntVar()
v0.set(1)
r1=Radiobutton(janela, text="Programação", variable=v0, value=1)
r2=Radiobutton(janela, text="Infra", variable=v0, value=2)
r2.place(x=0, y=300)
r1.place(x=80, y=300)

# Checkbutton

v1 = IntVar()
v2 = IntVar()
C1 = Checkbutton(janela, text="Futebol", variable=v1)
C2 = Checkbutton(janela, text="Tenis", variable=v2)
C1.place(x=0, y=280)
C2.place(x=80, y=280)

btn.pack()
janela.mainloop()