import random
import os
import json

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

#region Funcionamento

def Login(vUsuario,vCPF,vNumero):
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
    vNumero.append(10)
    print("\n\tBem Vindo -",vUsuario[CPF]["User"])
    print("O Número Limite que sera escolhido é -",vNumero[0])

    return True

def game(vUsuario,vCPF,vNumero):
  print("\n\t-=- ADVINHAÇÃO -=-")
  CPF = vCPF[0]
  if CPF in vUsuario:
    print("Adivinhe o Número")
    numero = random.randint(1,vNumero[0])
    chute = int(lerChute(vNumero))

    while chute != numero:
      print("Você Errou")
      if chute > numero:
        print("O Número é Menor")
        chute = int(lerChute(vNumero))
      else:
        print("O Número é Maior")
        chute = int(lerChute(vNumero))
    else:
      print("Você Acertou")

      vUsuario[CPF]["Saldo"] = vUsuario[CPF]["Saldo"] + 2.50
      vUsuario[CPF]["Acertos"] = vUsuario[CPF]["Acertos"] + 1
      save("Usuario.json",vUsuario)

      print("Acertos: ",vUsuario[CPF]["Acertos"])
      print("Deseja Jogar Novamente?")
      print("\t1. Sim")
      print("\t2. Não")

      op = options()
      if op == 1:
        game(vUsuario,vCPF,vNumero)
      else:
        print("Saindo...")
        return


  else:
    print("Usuário não encontrado")

#endregion

#region INPUT

def lerNome():
  nome = input("Insira o Nome: ")
  while nome.replace(" ","").isalpha() != True or len(nome) < 0:
    nome = input("Valor Inválido\nInsira o Nome: ")
  return nome

def lerChute(vNumero):
  chute = input("---> ")
  limite = vNumero[0]
  while chute.isdigit() != True or len(chute) > limite :
    chute = input("---> ")
  return chute

def lerSenha():
  senha = input("Insira senha:")
  while len(senha) < 6:
    senha = input("Valor Inválido\nInsira Senha: ")
  return senha

def lerNumero(vNumero):
  numero = input("Insira o Número: ")
  while numero.isdigit() != True:
    numero = input("Valor Inválido\nInsira o Número: ")
  vNumero.append(int(numero))

def lerCPF():
  cpf = input("Insira CPF: ")
  while cpf.replace(".", "").replace("-","").isdigit() != True or len(cpf) > 11:
    cpf = input("Valor Inválido\nInsira CPF: ")
  return cpf

#endregion

#region Menus / Opcoes

def menu():
  print("\n\t -=- ADVINHAÇÃO -=-")
  print("\n\t1. Login")
  print("\t2. Sair")

def menuJogo():
  print("\n\t -=- ADVINHAÇÃO -=-")
  print("\n\t1. Jogar")
  print("\t2. Configurações")
  print("\t3. Sair")

def options():

  op = input("---> ")
  while op not in ["1","2","3"]:
    op = input("Valor Inválido\n---> ")

  return int(op)

#endregion

def main():
  vUsuario = load("Usuario.json")
  vCPF = []
  vNumero = []
  menu()
  op = options()

  while op != 2:
    if op  == 1:
      if Login(vUsuario,vCPF,vNumero) == True:
        menuJogo()
        opi = options()
        while opi != 3:

          if opi == 1:
            game(vUsuario,vCPF,vNumero)
            menuJogo()
            opi = options()

          if opi == 2:
            print("-=- Insira o Número Máximo -=-")
            vNumero.clear()
            lerNumero(vNumero)
            menuJogo()
            opi = options()

        vCPF.clear()
        menu()
        op = options()

  print("Saindo...")

main()