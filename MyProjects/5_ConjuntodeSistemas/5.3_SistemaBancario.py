import json
import os

#region SAVE / LOAD

def save(nomeArquivo,lista):
  with open(nomeArquivo, "w") as arquivo:
    json.dump(lista, arquivo)


def load(nomeArquivo):
  if os.path.exists(nomeArquivo):
    with open(nomeArquivo,"r") as arquivo:
      return json.load(arquivo)
  else:
    print("Arquivo não encontrado")
    return {}

#endregion

#region FUNCIONAMENTO

def Login(vUsuario,vCPF):
  print("\n\t-=- LOGIN -=-")

  print("Login - CPF")
  CPF = lerCPF()
  Senha = lerSenha()

  while CPF not in vUsuario or vUsuario[CPF]["Senha"] != Senha:
    print("CPF ou Senha Inválidos")
    CPF = lerCPF()
    Senha = lerSenha()

  if Senha == vUsuario[CPF]["Senha"]:
    print("Login Realizado")
    vCPF.append(CPF)
    return True

def deposito(vUsuario,vCPF):
  print("\n\t-=- DEPOSITO -=-")
  CPF = vCPF[0]
  if CPF in vUsuario:
    valor = input("Insira o Valor: R$")
    while valor.replace(" ","").isdigit() != True or len(valor) < 0:
      valor = input("Valor Inválido\nInsira o Valor: ")

    vUsuario[CPF]["Saldo"] = vUsuario[CPF]["Saldo"] + float(valor)
    save("Usuario.json",vUsuario)
    print("Depósito Realizado")

  else:
    print("Usuário não encontrado")

def saque(vUsuario,vCPF):
  print("\n\t-=- SAQUE -=-")
  CPF = vCPF[0]
  if CPF in vUsuario:
    valor = input("Insira o Valor: R$")
    while valor.replace(" ","").isdigit() != True or len(valor) < 0:
      valor = input("Valor Inválido\nInsira o Valor: ")

    if float(valor) > vUsuario[CPF]["Saldo"]:
      print("Saldo Insuficiente")

    else:
      vUsuario[CPF]["Saldo"] = vUsuario[CPF]["Saldo"] - float(valor)
      save("Usuario.json",vUsuario)
      print("Saque Realizado")

  else:
    print("Usuário não encontrado")

def transferir(vUsuario,vCPF):
  print("\n\t-=- TRANSFERENCIA -=-")
  CPF = vCPF[0]
  if CPF in vUsuario:
    valor = input("Insira o Valor: R$")
    while valor.replace(" ","").isdigit() != True or len(valor) < 0:
      valor = input("Valor Inválido\nInsira o Valor: ")

    if float(valor) > vUsuario[CPF]["Saldo"]:
      print("Saldo Insuficiente")

    else:
      vUsuario[CPF]["Saldo"] = vUsuario[CPF]["Saldo"] - float(valor)
      print("Buscar Usuario Destinatario - CPF")
      CPF = lerCPF()
      while CPF not in vUsuario:
        print("Usuário não encontrado")
        print("Buscar Usuario Destinatario - CPF")
        CPF = lerCPF()

      vUsuario[CPF]["Saldo"] = vUsuario[CPF]["Saldo"] + float(valor)

      save("Usuario.json",vUsuario)
      print("Transferência Realizada")

  else:
    print("Usuário não encontrado")



def extrato(vUsuario,vCPF):
  print("\n\t-=- EXTRATO -=-")
  CPF = vCPF[0]
  if CPF in vUsuario:
    print("Saldo: R$",vUsuario[CPF]["Saldo"])
  else:
    print("Usuário não encontrado")

#endregion

#region READ INPUTS

def lerNome():
  nome = input("Insira o Nome: ")
  while nome.replace(" ","").isalpha() != True or len(nome) < 0:
    nome = input("Valor Inválido\nInsira o Nome: ")
  return nome

def lerCPF():
  cpf = input("Insira CPF: ")
  while cpf.replace(".", "").replace("-","").isdigit() != True or len(cpf) > 11:
    cpf = input("Valor Inválido\nInsira CPF: ")
  return cpf

def lerSenha():
  senha = input("Insira senha:")
  while len(senha) < 6:
    senha = input("Valor Inválido\nInsira Senha: ")
  return senha

#endregion

#region MENU / OPTIONS

def menuPrincipal():

  print("\n\t -=- SISTEMA BANCARIO -=-")
  print("\n\t1. Entrar")
  print("\t2. Sair")

def menuConta():

  print("\n\t -=- SISTEMA BANCARIO USUARIO -=-")
  print("\n\t1. Depositar")
  print("\t2. Sacar")
  print("\t3. Transferir")
  print("\t4. Extrato")
  print("\t5. Sair")

def options():

  op = input("---> ")
  while op not in ["1","2","3","4","5"]:
    op = input("Valor Inválido\n---> ")

  return int(op)

def main():
  vUsuario = load("Usuario.json")
  vCPF = []
  menuPrincipal()
  op = options()

  while op != 2:

    if op  == 1:

      if Login(vUsuario,vCPF) == True:
        menuConta()
        opi = options()

        while opi != 5:

          if opi == 1:
            deposito(vUsuario,vCPF)
            menuConta()
            opi = options()
          if opi == 2:
            saque(vUsuario,vCPF)
            menuConta()
            opi = options()
          if opi == 3:
            transferir(vUsuario,vCPF)
            menuConta()
            opi = options()
          if opi == 4:
            extrato(vUsuario,vCPF)
            menuConta()
            opi = options()

        vCPF.clear()
        menuPrincipal()
        op = options()

  print("Saindo...")
main()