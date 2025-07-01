
#region Funções dos Candidatos

def CadastroCandidato(vNumCandidatos,vVotos):

    Candidato = LerNumCandidatos()
    local = PesquisarNumCandidato(vNumCandidatos,Candidato)

    
    if local != -1:

        while Candidato == vNumCandidatos[local] :  
            print("Candidato Já Cadastrado!")

            Candidato = LerNumCandidatos()
            local = PesquisarNumCandidato(vNumCandidatos,Candidato)

    NumVotos = LerNumVotos()

    vNumCandidatos.append(Candidato)
    vVotos.append(NumVotos)

def PesquisarNumCandidato(vNumCandidatos,Candidato):
  
    local = -1
    i = 0
    while  i < len(vNumCandidatos):
        if Candidato == vNumCandidatos[i]:
            local = i
        i += 1
    return local

def ExcluirCandidato(vNumCandidatos,vVotos,candidato):

    local = PesquisarNumCandidato(vNumCandidatos,candidato)

    if local == -1:
        print("Candidato não Encontrado!")
    else:
        vNumCandidatos.pop(local)
        vVotos.pop(local)

def AtualizarCandidato(vNumCandidatos,vVotos,candidato):

    local = PesquisarNumCandidato(vNumCandidatos,candidato)
    if local == -1:
        print("Candidato não Encontrado")
    
    else:    
        print("\nNovos Dados Candidato")

        vNumCandidatos.pop(local)
        vVotos.pop(local)

        CadastroCandidato(vNumCandidatos,vVotos) 


def ListarCandidatos(vNumCandidatos,vVotos):
    print("\n\tLista de Candidatos\n")
    for i , e in enumerate(vNumCandidatos):
        print(vNumCandidatos[i],"/ Possui:",vVotos[i],"% Dos Votos")
    print("\tLista Finalizada")

def CandidatoMaisVotado(vNumCandidatos,vVotos):
    print("\n\tCandidato Mais Votado\n")
    local = None
    maior = -1

    for i,e in enumerate(vVotos):
        if e > maior:
            maior = e
            local = i

    print(vNumCandidatos[local],"/ Possui:",vVotos[local],"% Dos Votos")

#endregion

#region Entrada de Dados

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
    vNumCandidatos = []
    vVotos = []
    #endregion
    menu()
    op = opcoesNumericas()
     
    while op != 0:

        if op == 1:
            print("\n\tCadastro de Candidatos\n")
            CadastroCandidato(vNumCandidatos,vVotos)
            menu()
            op = opcoesNumericas()

        if op == 2:

            candidato = LerNumCandidatos()
            local = PesquisarNumCandidato(vNumCandidatos,candidato)
            print(vNumCandidatos[local],"/ Possui:",vVotos[local],"% Dos Votos")

            menu()
            op = opcoesNumericas()
    
        if op == 3:
            print("\n\tAlterar Dados do Candidato\n")
            candidato = LerNumCandidatos()
            AtualizarCandidato(vNumCandidatos,vVotos,candidato)
            menu()
            op = opcoesNumericas()  

        if op == 4:
            CandidatoMaisVotado(vNumCandidatos,vVotos)
            menu()
            op = opcoesNumericas() 

        if op == 5:
            print("\n\tExcluir Candidatos\n")
            candidato = LerNumCandidatos()
            ExcluirCandidato(vNumCandidatos,vVotos,candidato)
            menu()
            op = opcoesNumericas()

        if op == 6:
            ListarCandidatos(vNumCandidatos,vVotos)
            menu()
            op = opcoesNumericas()

    print("\nEncerrando Programa...")
main()
