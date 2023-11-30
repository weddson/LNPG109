
arquivo = open('meu_nome.txt', 'r', encoding='utf-8')
nomes = arquivo.read()

lista = nomes.split(';')

for n in lista:
    print(n)