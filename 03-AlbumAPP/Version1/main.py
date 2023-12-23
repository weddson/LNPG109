from tkinter import *

def listarAlbum():
    arquivo = open("bancodedados.txt", 'r', encoding='utf-8')
    tudo = arquivo.read()


    arquivo.close()

# Função de cadastro com nome do álbum, ano de lançamento, nome da banda ou artista, se é o álbum de lançamento do artista.
def cadastroAlbum():
    album = ''
    
    while album != 0:
        arquivo = open("bancodedados.txt", 'a', encoding='utf-8')
        print("Cadastro de álbum(para finalizar preencha o nome do álbum com 0)")
        album = input("Nome do álbum: ")
        if album == "0":
            print("Programa Finalizado")
            arquivo.close()
            exit()
        
        ano = input("Ano de lançamento: ")
        banda = input("Nome da banda ou artista: ")
        lancamento = input("É o álbum de lançamento do artista? (s/n): ")
        
        arquivo.write(album + "|")
        arquivo.write(ano + "|")
        arquivo.write(banda + "|")
        arquivo.write(lancamento + "|" + "\n")
        arquivo.close()

# Função de listar os albuns cadastrados.


# Um app com 2 botões, um para cadastrar e outro para listar os álbuns cadastrados.  
        

def main():
    def wincadf():
        wincad = Tk()
        wincad.title("Cadastro de Álbuns")
        wincad.geometry('1152x648')
        namefld = Entry(wincad, text="Nome do Álbum", bd=1)
        namefld.pack()
        anofld = Entry(wincad, text="Ano de lançamento", bd=1)
        anofld.pack()
        bandafld = Entry(wincad, text="Banda ou Artista", bd=1)
        bandafld.pack()
        v0=IntVar()
        v0.set(1)
        lancfld1 = Radiobutton(wincad, text="Sim", variable=v0, value=1)
        lancfld2 = Radiobutton(wincad, text="Não", variable=v0, value=2)
        lancfld1.place(x=100, y=80)
        lancfld2.place(x=100, y=100)
        btnentcad = Button(wincad, text="Cadastrar", command=cadastroAlbum)
        btnentcad.pack()
        wincad.mainloop()

    def winlistf():
        winlist = Tk()
        winlist.title("Lista de Álbuns")
        winlist.geometry('1152x648')
        winlist.mainloop()

    window = Tk()
    window.title("Álbuns")
    window.geometry('1152x648')
    btncad = Button(window, text="Cadastro de Álbuns", command=wincadf)
    btncad.pack()
    btnlist = Button(window, text="Listar Álbuns", command=winlistf)
    btnlist.pack()
    window.mainloop()

    

if __name__ == "__main__":

    main()