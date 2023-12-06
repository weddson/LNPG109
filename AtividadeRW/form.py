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
        arquivo.write(telefone + '\n')
        arquivo.close()

def buscaPorSexo(sexo):
    print('teste')

def buscaPorNome(nomeProcurado):
    print('teste')

# Print

def readForm():
    arquivo = open('meu_nome.txt', 'r', encoding='utf-8')
    tudo = arquivo.read()
    tudo = tudo.split('|')

    for linha in tudo:
        print(linha)

    # Nome: ...
    
    # Idade: ...

    # Masculino: ...
    
    # Telefone: ...

if __name__ == "__main__":
    #print('Preencha o formulário abaixo e para cancelar digite 0 na opção nome')
    readForm()
