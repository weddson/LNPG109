# Faça um programa como um formulário, que solicite do usuário as seguintes informações:
# Nome, Idade, Sexo(M ou F), Telefone
# Coloque o código dentro de uma função, e este código deve repetir até o usuário digitar "0" (para o nome) informando que ele deseja encerrar
# Dica
# Salve estas informações em um arquivo, separando cada dado pela barra vertical (pipe) "|"
# No final da linha (após telefone) adiciona um '\n'
# Verifique se o arquivo foi criado corretamente e os dados foram armazenados da maneira que você esperava.

# Cria função escreveform

def escreveForm():
    nome = ''
    # Enquanto nome for diferente de 0 repete o código
    while nome != '0':
        # Abre o arquivo para escrita
        arquivo = open('meu_nome.txt', 'a', encoding='utf-8')

        # Solicita os dados
        # Nome
        nome = input('Nome(0 para cancelar): ')
        if nome == '0':
            print('Programa finalizado.')
            exit()

        # Idade
        idade = input('Idade: ')

        #Sexo
        sexo = input('Sexo(M ou F): ')
        checkSex = ((sexo != "M" or sexo != "F") or (sexo != 'm' or sexo != 'f'))
        while checkSex == False:
            print('Sexo inválido')
            sexo = input('Sexo(M ou F): ')
            checkSex = ((sexo != "M" or sexo != "F") or (sexo != 'm' or sexo != 'f'))

        # Telefone
        telefone = input('Telefone: ')
        
        # Escreve no arquivo e fecha o arquivo
        arquivo.write(nome + '|')
        arquivo.write(idade + '|')
        arquivo.write(sexo + '|')
        arquivo.write(telefone + '|' +'\n')
        arquivo.close()

def buscaPorSexo(sexo):
    arquivo = open('meu_nome.txt', 'r', encoding='utf-8')
    tudo = arquivo.read()
    tudo = tudo.split('|')
    n = 0
    while n < len(tudo)-1:
        if tudo[n+2] == sexo:
            print('Nome: ' + tudo[n].strip('\n'))
            print('Idade: ' + tudo[n+1] + ' anos')
            tudo[n+2] = tudo[n+2] == 'M' and 'Masculino' or 'Feminino'
            print('Sexo: ' + tudo[n+2])
            print('Telefone: ' + tudo[n+3].strip('\n'))
        n += 4
            


def buscaPorNome(nomeProcurado):
    arquivo = open('meu_nome.txt', 'r', encoding='utf-8')
    tudo = arquivo.read()
    tudo = tudo.split('|')
    n = 0
    while n < len(tudo)-1:
        if tudo[n].strip('\n') == nomeProcurado:
            print('Nome: ' + tudo[n].strip('\n'))
            print('Idade: ' + tudo[n+1] + ' anos')
            tudo[n+2] = tudo[n+2] == 'M' and 'Masculino' or 'Feminino'
            print('Sexo: ' + tudo[n+2])
            print('Telefone: ' + tudo[n+3].strip('\n'))
        n += 4

def readForm():
    arquivo = open('meu_nome.txt', 'r', encoding='utf-8')
    tudo = arquivo.read()
    tudo = tudo.split('|')

    for linha in tudo:

        if len(linha) > 3 and not linha.isdigit():
            print('Nome: ' + linha.strip('\n'))
        elif len(linha) <= 3 and linha.isdigit():
            print('Idade: ' + linha + ' anos')
        elif linha == 'M' or linha == 'F':
            if linha == 'M':
                linha = 'Masculino'
            else:
                linha = 'Feminino'
            print('Sexo: ' + linha)
        elif len(linha) > 3:
            print('Telefone: ' + linha.strip('\n'))

if __name__ == "__main__":
    #print('Preencha o formulário abaixo e para cancelar digite 0 na opção nome')
    buscaPorNome("Wedson")
