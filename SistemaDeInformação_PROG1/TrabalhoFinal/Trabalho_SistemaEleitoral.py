
#region Funções dos Candidatos

def CadastroCandidato(vCandidatos,vNumCandidatos,vVotos):

    print("\n\tCadastro de Candidatos\n")
    Nome = LerNomes()
    NumCandidatos = LerNumCandidatos()
    NumVotos = LerNumVotos()

    vCandidatos.append(Nome)
    vNumCandidatos.append(NumCandidatos)
    vVotos.append(NumVotos)

def PesquisarNumCandidato(vCandidatos,vNumCandidatos,vVotos):

    print("\nPesquisar Número dos Candidatos\n")
    e = LerNumCandidatos()
    local = None

    while e not in vNumCandidatos:
        print("Candidato não Encontrado")
        e = LerNumCandidatos()

    for i , e in enumerate(vNumCandidatos):
        local = i

    print(vNumCandidatos[local],"-",vCandidatos[local],"/ Possui:",vVotos[local],"% Dos Votos")
    return local

def ExcluirCandidato(vCandidatos,vNumCandidatos,vVotos,):
    print("\n\tExcluir Candidatos\n")

    local = PesquisarNumCandidato(vCandidatos,vNumCandidatos,vVotos)

    vCandidatos.pop(local)
    vNumCandidatos.pop(local)
    vVotos.pop(local)

def AtualizarCandidato(vCandidatos,vNumCandidatos,vVotos):
    print("\n\tAlterar Dados do Candidato\n")

    local = PesquisarNumCandidato(vCandidatos,vNumCandidatos,vVotos)

    print("\nNovos Dados Candidato")
    vCandidatos[local] = LerNomes()
    vNumCandidatos[local] = LerNumCandidatos()
    vVotos[local] = LerNumVotos()

def ListarCandidatos(vCandidatos,vNumCandidatos,vVotos):
    print("\n\tLista de Candidatos\n")
    for i , e in enumerate(vNumCandidatos):
        print(vNumCandidatos[i],"-",vCandidatos[i],"/ Possui:",vVotos[i],"% Dos Votos")
    print("\tLista Finalizada")

def CandidatoMaisVotado(vCandidatos,vNumCandidatos,vVotos):
    print("\n\tCandidato Mais Votado\n")
    local = None
    maior = -1

    for i,e in enumerate(vVotos):
        if e > maior:
            maior = e
            local = i

    print(vNumCandidatos[local],"-",vCandidatos[local],"/ Possui:",vVotos[local],"% Dos Votos")

#endregion

#region Entrada de Dados

def LerNomes():
    Nome = input("Nome Candidato: ")
    while Nome.replace(" ","").isalpha() == False or len(Nome) < 0 or len(Nome) > 100:
        print("\nValor Inválido")
        Nome = input("Nome Candidato: ")
    return Nome

def LerNumCandidatos():
    NumCandidato = input("Número do Candidato: ")
    while NumCandidato.isdigit() != True or len(NumCandidato) > 3:
        print("\nValor Inválido") 
        NumCandidato = input("Número do Candidato: ")
    return NumCandidato

def LerNumVotos():
    NumVotos = input("Porcentagem de Votos: ")
    while NumVotos.replace(".","").isdigit() != True or float(NumVotos) < 0 or float(NumVotos) > 100:
        print("\nValor Inválido")
        NumVotos = input("Porcentagem de Votos: ")
    return float(NumVotos)

#endregion

#region Menu/Opções

def opcoesNumericas():
    opcao = input("Escolha a sua opção: ")
    while opcao.isdigit() != True or int(opcao) < 0 or int(opcao) > 6:
        print("Valor Digitado Inválido")
        opcao = input("Escolha a sua opção: ")
    return int(opcao)

def menu():
    print("\n\tSISTEMA ELEITORAL\n")
    print("1 – Inserir candidato")
    print("2 – Pesquisar por número")
    print("3 – Alterar")
    print("4 – Mais votado")
    print("5 – Excluir")
    print("6 - Listar")
    print("0 – Sair")

#endregion

def main():
    #region Variáveis Iniciais
    vCandidatos = []
    vNumCandidatos = []
    vVotos = []
    #endregion
    menu()
    op = opcoesNumericas()
     
    while op != 0:

        if op == 1:
            CadastroCandidato(vCandidatos,vNumCandidatos,vVotos)
            menu()
            op = opcoesNumericas()

        if op == 2:
            PesquisarNumCandidato(vCandidatos,vNumCandidatos,vVotos)
            menu()
            op = opcoesNumericas()
    
        if op == 3:
            AtualizarCandidato(vCandidatos,vNumCandidatos,vVotos)
            menu()
            op = opcoesNumericas()  

        if op == 4:
            CandidatoMaisVotado(vCandidatos,vNumCandidatos,vVotos)
            menu()
            op = opcoesNumericas() 

        if op == 5:
            ExcluirCandidato(vCandidatos,vNumCandidatos,vVotos)
            menu()
            op = opcoesNumericas()

        if op == 6:
            ListarCandidatos(vCandidatos,vNumCandidatos,vVotos)
            menu()
            op = opcoesNumericas()

    print("\nEncerrando Programa...")
main()
