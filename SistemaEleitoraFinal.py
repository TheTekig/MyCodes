import json
import os
#SOCORRO DEUSS
#region -=- SAVE/LOAD -=-

def salvar(nomeArquivo,lista):
  with open(nomeArquivo, "w") as arquivo:
    json.dump(lista, arquivo)

def load(nomeArquivo):
  if os.path.exists(nomeArquivo):
    with open(nomeArquivo,"r") as arquivo:
      return json.load(arquivo)
  else:
    print("Arquivo não encontrado")
    return []

#endregion

#region -=- VALIDAÇÕES -=-

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

#region -=- SETUP CANDIDATOS -=-

def cadastroCandidato(vCandidato, vNumeroCandidato):
  print("\n\t-=- Cadastro de Candidatos -=-\n")
  print("Nome do Candidato:")
  nome = CargoEConcorrente()
  numero = validacaoDigitos()

  while numero in vNumeroCandidato:

    numero = validacaoDigitos()

  vCandidato.append(nome)
  vNumeroCandidato.append(numero)
  salvar("candidatos.json",vCandidato)
  salvar("numeroCandidato.json",vNumeroCandidato)

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
  print("Nome do Candidato:")
  nome = CargoEConcorrente()
  if nome in vCandidato:
    local = vCandidato.index(nome)
    vCandidato[local] = input("Novo nome de Candidato: ")
    vNumeroCandidato[local] = validacaoDigitos()
    salvar("candidatos.json",vCandidato)
    salvar("numeroCandidato.json",vNumeroCandidato)
    print("\n\t-=- Candidato Atualizado -=-\n")

def removerCandidato(vCandidato, vNumeroCandidato):
  print("\n\t-=- Remoção de Candidatos -=-\n")
  print("Nome do Candidato: ")
  nome = CargoEConcorrente()

  if nome in vCandidato:
    local = vCandidato.index(nome)
    vCandidato.pop(local)
    vNumeroCandidato.pop(local)
    salvar("candidatos.json",vCandidato)
    salvar("numeroCandidato.json",vNumeroCandidato)
    print("\n\t-=- Candidato Removido -=-\n")

#endregion

#region -=- VOTAÇÃO -=-

def mediaVotos(vVotos):

  print("\n\t-=- Média de Votos -=-\n")
  i = 0
  soma = 0
  while i < len(vVotos):
    soma = soma + vVotos[i]
    i = i + 1
  media = soma / len(vVotos)
  print(media)

def quantidadeVotos(vVotos,vCandidato,vNumeroCandidato):

  print("\n\t-=- Quantidade de Votos -=-\n")

  if len(vVotos) == 0:
    print("\n\t-=- Lista Vazia -=-\n")
    return

  else:
    i = 0
    while i < len(vVotos):
      print(vCandidato[i] , "-" , vVotos[i])
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
    salvar("votos.json",vVotos)
    print("\n\t-=- Voto Registrado -=-\n")
  else:
    print("\n\t-=- Voto Cancelado -=-\n")
    votacaoCandidatos(vVotos,vCandidato,vNumeroCandidato)

def CandidatoVencedor(vVotos,vCandidato,vNumeroCandidato,vSegundoTurno,vCPF):

    if len(vVotos) == 0:
        print("\n\t-=- Não Possui Candidatos -=-\n")
        return

    print("\n\t-=- RESULTADOS -=-\n")

    maior = -1
    local = None

    for i, e in enumerate(vVotos):
        if e > maior:
            maior = e
            local = i

    vSegundoTurno.clear()

    for i, votos in enumerate(vVotos):
        if votos == maior:
            vSegundoTurno.append(vNumeroCandidato[i])

    if len(vSegundoTurno) > 1:
        print("\nSegundo Turno:")
        for numero in vSegundoTurno:
            local = vNumeroCandidato.index(numero)
            print(vNumeroCandidato[local], "-", vCandidato[local])
    else:

        local = vNumeroCandidato.index(vSegundoTurno[0])
        print("\nO candidato", vCandidato[local], "-", vNumeroCandidato[local],
              "venceu com", vVotos[local], "votos")

        vSegundoTurno.clear()
        
        

    vCPF.clear()
    salvar("cpf.json",vCPF)
    print("Total de Votos Recebido: ",len(vCPF),"\n")

    print("\n\t-=- Fim do Resultado -=-\n")



def ZerarVotosCandidatos(vVotos):
  i = 0
  while i < len(vVotos):
    vVotos[i] = 0
    i = i + 1
  salvar("votos.json",vVotos)

#endregion

#region -=- SETUP ADMs -=-

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
  salvar("administradores.json",vAdministradores)
  salvar("senhas.json",vSenhas)
  print("\n\t-=- Administrador Cadastrado -=-\n")

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
    salvar("administradores.json",vAdministradores)
    salvar("senhas.json",vSenhas)
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
    salvar("administradores.json",vAdministradores)
    salvar("senhas.json",vSenhas)
    print("\n\t-=- Administrador Atualizado -=-\n")

def imprimirAdm(vAdministradores):

  print("\n\t-=- Lista de Administradores -=-\n")
  i = 0
  while i < len(vAdministradores):
    print(vAdministradores[i])
    i = i + 1
  print("\n\t-=- Fim da Lista -=-\n")

#endregion

#region -=- CPF FUNCTIONS -=-

def lerCPF(vCPF):
  print("\n\t -=- Validação Para Votar -=-")
  cpf = input("CPF: ")
  while cpf.replace(" ","").isdigit() != True or len(cpf) != 11 or cpf in vCPF:
    if cpf in vCPF:
      cpf = input("\n\t-=-CPF Já Votou-=-\nCPF: ")
    else:
      cpf = input("\n\t-=-Valor Digitado Invalido-=-\nCPF: ")

  if cpf not in vCPF:
    vCPF.append(cpf)
    salvar("cpf.json",vCPF)
    return False
  else:
    return True

def removerCPF(vCPF):
  print("\n\t-=- Remoção de CPF -=-\n")
  print("Deseja Remover um CPF ou Todos? (R/T)")
  op = input("Digito: ")
  while op.upper() != "R" and op.upper() != "T":
    op = input("\n\t-=-Valor Digitado Invalido-=-\nDigito: ")

  if op.upper() == "R":
    cpf = input("CPF: ")
    if cpf in vCPF:
      local = vCPF.index(cpf)
      vCPF.pop(local)
      salvar("cpf.json",vCPF)
      print("\n\t-=- CPF Removido -=-\n")
    else:
      print("\n\t-=- CPF Não Encontrado -=-\n")

  else:
    vCPF.clear()
    salvar("cpf.json",vCPF)
    print("\n\t-=- CPF Removido -=-\n")

#endregion

#region -=- MENU´s -=-

def menuPrincipal():
  print("\n\t-=- Menu -=-")
  print("Digite 0 para encerrar o programa")
  print("Digite 1 para Votar")
  print("Digite 2 para imprimir Candidatos")
  print("Digite 3 para imprimir Candidato Vencedor")
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
  print("Digite 5 para remover CPF")

#endregion

#region -=- RUN -=-

def main():

#region -=- VARIAVEIS INICIAIS -=-

  vAdministradores = load("administradores.json")
  vAdministradores.append("adm")
  vSenhas = load("senhas.json")
  vSenhas.append("123456")
  vCandidatos = load("candidatos.json")
  vNumeroCandidato = load("numeroCandidato.json")
  vVotos = load("votos.json")
  vCPF = load("cpf.json")
  vSegundoTurno = []

#endregion

  print("\n\t-=-SISTEMA DE ELEIÇÕES-=-")
  menuPrincipal()
  opv = opn()
  while opv != 0:

    if opv > 4:
      print("\n\t-=-Opção Inválida-=-\n")
      menuPrincipal()
      opv = opn()

    if opv == 1:
      if lerCPF(vCPF) == True:
        menuPrincipal()
        opv = opn()
      votacaoCandidatos(vVotos,vCandidatos,vNumeroCandidato)
      menuPrincipal()
      opv = opn()
    if opv == 2:
      imprimirCandidato(vCandidatos,vNumeroCandidato)
      menuPrincipal()
      opv = opn()

    if opv == 3:
      CandidatoVencedor(vVotos,vCandidatos,vNumeroCandidato,vSegundoTurno,vCPF)
      ZerarVotosCandidatos(vVotos)
      menuPrincipal()
      opv = opn()

    if opv == 4:

      if loginAdm(vAdministradores,vSenhas) == True:
        menuADM()
        opa = opn()
        while opa != 0:

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
            quantidadeVotos(vVotos,vCandidatos,vNumeroCandidato)
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

              if opi > 5:
                print("\n\t-=-Opção Inválida-=-\n")
                gerenciamentoAdm()
                opi = opn()

              if opi == 1:
                cadastroAdm(vAdministradores,vSenhas)
                gerenciamentoAdm()
                opi = opn()

              if opi == 2:
                imprimirAdm(vAdministradores)
                gerenciamentoAdm()
                opi = opn()

              if opi == 3:
                removerAdm(vAdministradores,vSenhas)
                gerenciamentoAdm()
                opi = opn()

              if opi == 4:
                atualizarAdm(vAdministradores,vSenhas)
                gerenciamentoAdm()
                opi = opn()

              if opi == 5:
                removerCPF(vCPF)
                gerenciamentoAdm()
                opi = opn()

            menuADM()
            opa = opn()

        menuPrincipal()
        opv = opn()

      else:
        print("\n\t-=- Login Inválido -=-\n")
        menuPrincipal()
        opv = opn()

  print("\nEncerrando Programas...")

  print("Total de Votos Recebido: ",len(vCPF),"\n")

#endregion

main()
