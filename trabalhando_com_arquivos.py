def lerNomes():
    arquivo = open('meu_nome.txt', 'r', encoding='utf-8')
    nomes = arquivo.read()
    lista = nomes.split(' ')
    for n in lista:
        print(n)

def escreveNomes(nomes):
    arquivo = open('meu_nome.txt', 'a', encoding='utf-8')
    arquivo.write(nomes)
    arquivo.close()

def main():
    lerNomes()
    escreveNomes('Maria Rocha Caravalho \n')

if __name__ == "__main__":
    main()