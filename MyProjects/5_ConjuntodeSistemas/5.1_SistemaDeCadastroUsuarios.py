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

#region USER CONFIG

def cadastroUsuario(vUsuario):

  print("\n\t-=- CADASTRO DE USUÁRIO -=-")

  print("\nRegistrar Nome")
  User = lerNome()
  while User in vUsuario:
    print("Usuário Já Cadastrado\nRegistrar Nome")
    User = lerNome()

  print("Registrar CPF")
  CPF = lerCPF()
  while CPF in vUsuario:
    print("CPF já Cadastrado\nRegistrar CPF")
    CPF  = lerCPF()

  print("Registrar Senha")
  Senha = lerSenha()

  print("Confirmar Senha")
  ConfirmSenha = lerSenha()

  while Senha != ConfirmSenha:
    print("Senhas não Conferem")



  vUsuario[CPF] = {

             "User" : User,
             "Senha": Senha,
             "Saldo" : 0,
             "Acertos": 0

  }

  save("Usuario.json",vUsuario)
  print("Usuário Cadastrado")

def atualizarUsuario(vUsuario):
  print("\n\t-=- ATUALIZAÇÃO DE USUÁRIO -=-")
  print("Buscar Usuario - CPF")
  CPF = lerCPF()

  if CPF in vUsuario:
    nome = lerNome()
    senha = lerSenha()
    confirmSenha = lerSenha()
    while senha != confirmSenha:
      print("Senhas não Conferem")

    vUsuario[CPF] = {

             "User" : nome,
             "Senha": senha

    }
    save("Usuario.json",vUsuario)
    print("Usuário Atualizado")

  else:
    print("Usuário não encontrado")

def removerUsuario(vUsuario):
  print("\n\t-=- REMOÇÃO DE USUÁRIO -=-")
  print("Buscar Usuario - CPF")
  CPF = lerCPF()

  if CPF in vUsuario:
    vUsuario.pop(CPF)

    save("Usuario.json",vUsuario)
    print("Usuário Removido")

  else:
    print("Usuário não encontrado")

def listarUsuario(vUsuario):
  print("\n\t-=- LISTA DE USUÁRIOS -=-")

  if len(vUsuario) == 0:
    print("Nenhum Usuário Cadastrado")
    return

  for CPF in vUsuario:

    print("\nCPF: ",CPF)
    print("Nome: ",vUsuario[CPF]["User"])


  print("\n")

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

def menu():

  print("\n\t -=- SISTEMA CADASTRO DE USUÁRIOS -=-")
  print("\n\t1. Cadastrar")
  print("\t2. Listar Usuários")
  print("\t3. Atualizar Usuários")
  print("\t4. Remover Usuários")
  print("\t5. Sair")

def options():

  op = input("---> ")
  while op not in ["1","2","3","4","5"]:
    op = input("Valor Inválido\n---> ")

  return int(op)

#endregion

def main():

  #region Variaveis Iniciais

  vUsuario = load("Usuario.json")

  #endregion

  menu()
  op = options()

  while op != 5:

    if op  == 1:
      cadastroUsuario(vUsuario)
      menu()
      op = options()

    if op == 2:
      listarUsuario(vUsuario)
      menu()
      op = options()

    if op == 3:
      atualizarUsuario(vUsuario)
      menu()
      op = options()

    if op == 4:
      removerUsuario(vUsuario)
      menu()
      op = options()

  print("Saindo...")
main()