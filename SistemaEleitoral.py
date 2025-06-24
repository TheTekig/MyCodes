
#region -=-Validações-=-

def validacaoDigitos():
  digito = input("Numero do candidato: ")
  while digito.isdigit() != True or len(digito) < 0 or len(digito) > 3:
    digito = input("\n\t-=-Valor Digitado Invalido-=-\nNumero do candidato: ")
  return digito

def CargoEConcorrente():
  nome = input("")
  while nome.isalpha() != True or len(nome) < 0:
    nome = input("Valor Inválido")
  return nome

def opn():
  op = input("Digito: ")
  while op.isdigit() != True or int(op) < 0 or int(op) > 6:
    op = input("\n\t-=-Valor Digitado Invalido-=-\nDigito: ")

  return int(op)

def opl():
  op = input("Digito: ")
  while op.upper() != "S" and op.upper() != "N":
    op = input("\n\t-=-Valor Digitado Invalido-=-\nDigito: ")
  return op.upper()

#endregion

#region -=-CANDIDATOS SETUP-=-

def cadastroCandidato(vCandidato, vNumeroCandidato):
  print("\n\t-=- Cadastro de Candidatos -=-\n")
  print("Nome do Candidato:")
  nome = CargoEConcorrente()
  numero = validacaoDigitos()

  while numero in vNumeroCandidato:

    numero = validacaoDigitos()

  vCandidato.append(nome)
  vNumeroCandidato.append(numero)

def imprimirCandidato(vCandidato, vNumeroCandidato):

  print("\n\t-=- Lista de Candidatos -=-\n")
  i = 0
  if len(vCandidato) == 0:
    print("\n\t-=- Lista Vazia -=-\n")
  else:
    while i < len(vCandidato):
      print(vCandidato[i] , " - " , vNumeroCandidato[i])
      i = i + 1
  print("\n\t-=- Fim da Lista -=-\n")

def atualizarCandidato(vCandidato, vNumeroCandidato):

  print("\n\t-=- Atualização de Candidatos -=-\n")
  nome = CargoEConcorrente()
  if nome in vCandidato:
    local = vCandidato.index(nome)
    vCandidato[local] = input("Novo nome de Candidato: ")
    vNumeroCandidato[local] = validacaoDigitos()

def removerCandidato(vCandidato, vNumeroCandidato):
  print("\n\t-=- Remoção de Candidatos -=-\n")
  nome = CargoEConcorrente()

  if nome in vCandidato:
    local = vCandidato.index(nome)
    vCandidato.pop(local)
    vNumeroCandidato.pop(local)
    print("\n\t-=- Candidato Removido -=-\n")

def mediaVotos(vVotos):

  print("\n\t-=- Média de Votos -=-\n")
  i = 0
  soma = 0
  while i < len(vVotos):
    soma = soma + vVotos[i]
    i = i + 1
  media = soma / len(vVotos)
  print(media)

def quantidadeVotos(vVotos,vCandidato):

  print("\n\t-=- Quantidade de Votos -=-\n")
  i = 0
  while i < len(vVotos):
    print(vCandidato[i] , " - " , vVotos[i])
    i = i + 1
  print("\n\t-=- Fim da Lista -=-\n")

def votacaoCandidatos(vVotos,vCandidato,vNumeroCandidato):

  print("\n\t-=- Votação -=-\n")
  numero = validacaoDigitos()
  while numero not in vNumeroCandidato:
    print("\n\t-=- Número de Candidato Inválido -=-\n")
    numero = validacaoDigitos()

  local = vNumeroCandidato.index(numero)
  print(vNumeroCandidato[local]," - ",vCandidato[local])
  print("\nDeseja Votar nesse Candidato? (S/N)")
  op = opl()

  if op == "S":
    vVotos[local] = vVotos[local] + 1
    print("\n\t-=- Voto Registrado -=-\n")
  else:
    print("\n\t-=- Voto Cancelado -=-\n")
    votacaoCandidatos(vVotos,vCandidato,vNumeroCandidato)

def vitoriaCandidato(vVotos,vCandidato,vNumeroCandidato):
  
  maior = -999

  for i in vVotos:
    if i > maior:
      maior = i
      localizacao = vVotos.index(i)                
  print("O candidato" , vCandidato[localizacao],"-",vNumeroCandidato[localizacao]  , " foi eleito com" , vVotos[localizacao] , " Votos\n" )
  
  for i , e in vVotos[i]:
    vVotos[i] = 0
    

#endregion

#region -=-ADMs Functions-=-

def cadastroAdm(vAdministradores,vSenhas):

  print("\n\t-=- Cadastro de Administradores -=-\n")
  print("Usuario:")
  nome = CargoEConcorrente()
  while nome in vAdministradores:
    print("Valor Inválido\nUsuario:")
    nome = CargoEConcorrente()

  senha = input("Senha: ")
  while len(senha) < 6:
    senha = input("Valor Inválido")

  vAdministradores.append(nome)
  vSenhas.append(senha)

def loginAdm(vAdministradores,vSenhas):
  print("\n\t-=- Login de Administradores -=-\n")
  nome = input("Usuario: ")
  while nome.isalpha() != True or len(nome) < 0:
    nome = input("Valor Inválido")
  senha = input("Senha: ")
  while len(senha) < 6:
    senha = input("Valor Inválido")

  if nome in vAdministradores and senha in vSenhas:
    return True
  else:
    return False

def removerAdm(vAdministradores,vSenhas):
  print("\n\t-=- Remoção de Administradores -=-\n")
  nome = input("Usuario: ")
  while nome.isalpha() != True or len(nome) < 0:
    nome = input("Valor Inválido")
  if nome in vAdministradores:
    local = vAdministradores.index(nome)
    vAdministradores.pop(local)
    vSenhas.pop(local)
    print("\n\t-=- Administrador Removido -=-\n")

def atualizarAdm(vAdministradores,vSenhas):
  print("\n\t-=- Atualização de Administradores -=-\n")
  nome = input("Usuario: ")
  while nome.isalpha() != True or len(nome) < 0:
    nome = input("Valor Inválido")
  if nome in vAdministradores:
    local = vAdministradores.index(nome)
    vAdministradores[local] = input("Novo Usuario: ")
    vSenhas[local] = input("Nova Senha: ")

def imprimirAdm(vAdministradores):
  print("\n\t-=- Lista de Administradores -=-\n")
  i = 0
  while i < len(vAdministradores):
    print(vAdministradores[i])
    i = i + 1
  print("\n\t-=- Fim da Lista -=-\n")

#endregion

#region -=-MENUS-=-

def menuPrincipal():
  print("\n\t-=- Menu -=-")
  print("Digite 0 para encerrar o programa")
  print("Digite 1 para Votar")
  print("Digite 2 para imprimir Candidatos")
  print("Digite 3 para Encerrar a Eleição")
  print("Digite 4 para entrar no menu administração")

def menuADM():
  print("\n\t-=- Menu ADM -=-")
  print("Digite 0 para retornar ao menu principal")
  print("Digite 1 para cadastrar Candidatos")
  print("Digite 2 para imprimir Candidatos Cadastrados")
  print("Digite 3 para remover Candidatos")
  print("Digite 4 para atualizar Candidatos")
  print("Digite 5 para média de votos dos Candidatos")
  print("Digite 6 para Gerenciamento de Administradores")

def gerenciamentoAdm():
  print("\n\t-=- Gerenciamento de ADM -=-")
  print("Digite 0 para retornar ao menu ADM principal")
  print("Digite 1 para cadastrar Administradores")
  print("Digite 2 para imprimir Administradores Cadastrados")
  print("Digite 3 para remover Administradores")
  print("Digite 4 para atualizar Administradores")

#endregion

def main():

#region -=-Lista/Variáveis Iniciais-=-

  vAdministradores = []
  vAdministradores.append("adm")
  vSenhas = []
  vSenhas.append("123456")
  vCandidatos = []
  vNumeroCandidato = []
  vVotos = []

#endregion

  print("\n\t-=-SISTEMA DE ELEIÇÕES-=-")
  
# -=-MENU PRINCIPAL-=-

  menuPrincipal()
  opv = opn()
  while opv != 0:

#Maximo de opções possiveis no menu principal
    if opv > 4:
      print("Valor Inválido")
      menuPrincipal()
      opv = opn()

    if opv == 1:
        votacaoCandidatos(vVotos,vCandidatos,vNumeroCandidato)
        menuPrincipal()
        opv = opn()

    if opv == 2:
        imprimirCandidato(vCandidatos,vNumeroCandidato)
        menuPrincipal()
        opv = opn()

    if opv == 3:
        print("\nEncerrando Eleições...")
        quantidadeVotos(vVotos,vCandidatos)
        vitoriaCandidato(vVotos,vCandidatos,vNumeroCandidato)

    if opv == 4:

#   -=-LOGIN ADM-=-
      if loginAdm(vAdministradores,vSenhas) == True:
        menuADM()
        opa = opn()
        while opa != 0:

#Maximo de opções possiveis no menuADM
          if opa > 6:
            print("Valor Inválido")
            menuADM()
            opa = opn()   

          if opa == 1:
            cadastroCandidato(vCandidatos,vNumeroCandidato)
            vVotos.append(0)
            menuADM()
            opa = opn()

          if opa == 2:
            imprimirCandidato(vCandidatos,vNumeroCandidato)
            menuADM()
            opa = opn()

          if opa == 3:
            removerCandidato(vCandidatos,vNumeroCandidato)
            menuADM()
            opa = opn()

          if opa == 4:
            atualizarCandidato(vCandidatos,vNumeroCandidato)
            menuADM()
            opa = opn()

          if opa == 5:
            quantidadeVotos(vVotos,vCandidatos)
            print("Deseja ver a médias de votos? (S/N)")
            L_op = opl()
            if L_op == "S":
              mediaVotos(vVotos)
            menuADM()
            opa = opn()

          if opa == 6:
            gerenciamentoAdm()
            opi = opn()

            while opi != 0:
#Maximo de opções possiveis no gerenciamentoAdm             
              if opi > 4:
                print("Valor Inválido")
                menuADM()
                opi = opn()                

              if opi == 1:
                cadastroAdm(vAdministradores,vSenhas)
                menuADM()
                opi = opn()

              if opi == 2:
                imprimirAdm(vAdministradores)
                menuADM()
                opi = opn()

              if opi == 3:
                removerAdm(vAdministradores,vSenhas)
                menuADM()
                opi = opn()

              if opi == 4:
                atualizarAdm(vAdministradores,vSenhas)
                menuADM()
                opi = opn()


            menuADM()
            opa = opn()

        menuPrincipal()
        opv = opn()

      else:
        print("\n\t-=- Login Inválido -=-\n")
        menuPrincipal()
        opv = opn()

  print("Encerrando Programa...")

main()
