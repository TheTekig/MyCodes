def adicionar_nomes():
    nomes = input("Insira seu Nome ---> ")
    while nomes.replace(" ","").isalpha != True or len(nomes) < 1:
        nomes = input("Nome Inválido\nInsira seu Nome ---> ") 
    
    return nomes

def adicionar_telefones():
    telefone = input ("Insira seu Número ---> ")
    while telefone.isdigit != True or len(telefone) < 9:
        telefone = input ("Número de Telefone Inválido\nInsira o Número ---> ")

    return telefone

def adicionar_Dados(vNomes,vTelefones):

    telefone = adicionar_telefones()
    nomes = adicionar_nomes()

    vNomes.append(nomes)
    vTelefones.append(telefone)

def imprimirLetra():



def lerDados():
    firstLetter = input("Digite a primeira Letra do Contato ---> ")
    while len(firstLetter) != 1:
        firstLetter = input("Entrada inválida\nDigite a primeira Letra do Contato ---> ")

    return str(firstLetter)

def menu_op():
    op_ = input("Digite a opção desejada: ")
    while op_.isnumeric() == False or int(op_) < 1 or int(op_) > 4:
        print("A opção deve ser um número e estar entre 1 e 4.")
        op_ = input("Digite a opção desejada: ")
    return op_

def print_opcoes():
    print("\n\t-=-Agenda Eletrônica-=-")
    print("1 - Cadastrar Nome/Número")
    print("2 - Lista de Usuários Cadastrados")
    print("3 - Buscador de Usuários")
    print("4 - Sair")

def print_tabela(vNomes,vTelefones,cont):


    print(vNomes[cont])
    print(vTelefones[cont])

def main_():
    vNomes = []
    vTelefones = []
 

    print_opcoes()
    op_ = menu_op()    
    while op_ != 4:
        if op_ == 1:

            adicionar_Dados()

        if op_ == 2:

            cont = 0

            for i in vNomes:
                print_tabela(cont)
                cont = cont + 1

        if op_ == 3:
                
                f_letter = lerDados()
                for x in vNomes:
                    if x[0] == f_letter:
                        imprimirLetra()

    

    
                        
              
        




    


    imprimirLetra(vNomes, vTelefones)
    

main_()