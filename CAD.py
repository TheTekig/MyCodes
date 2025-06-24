import json
import os

def salvar(lista, nomeArquivo):
  with open(nomeArquivo, "w") as arquivo:
    json.dump(lista, arquivo)

def carregar(nomeArquivo):
  if os.path.exists(nomeArquivo):
    with open(nomeArquivo,"r") as arquivo:
      return json.load(arquivo)
  else:
    print("Arquivo não encontrado")
    return []

def lerNome(vetNomes):
  nome = input("Nome: ")
  while nome.replace(" ","").isalpha() != True or nome in vetNomes:
    if nome in vetNomes:
      nome = input("\n\t-=-Nome Já possui Cadastro-=-\nNome: ")
    else:
      nome = input("\n\t-=-Valor Digitado Invalido-=-\nNome: ")
  return nome

def lerTelefone(vetTelefones):
  telefone = input("Telefone: ")
  while telefone.replace(" ","").isdigit() != True or len(telefone) != 9 or telefone in vetTelefones:
    if telefone in vetTelefones:
      telefone = input("\n\t-=-Telefone Já possui Cadastro-=-\nTelefone: ")
    else:
      telefone = input("\n\t-=-Valor Digitado Invalido-=-\nTelefone: ")

  return telefone

def cadastroNome(vetNomes):

  nome = lerNome(vetNomes)
  vetNomes.append(nome)
  salvar(vetNomes, "nomes.json")

def cadastroTelefone(vetTelefones):

    telefone = lerTelefone(vetTelefones)
    vetTelefones.append(telefone)
    salvar(vetTelefones, "telefones.json")

def listaContatos(vetNomes,vetTelefones):
    print("\n\t-=- Lista de Contatos -=-\n")

    i = 0
    while i < len(vetNomes):
      print(vetNomes[i] , " - " , vetTelefones[i])
      i = i + 1

    print("\n\t-=- Fim da Lista -=-\n")

def atualizarCadastro(vetNomes,vetTelefones):
  print("\n\t-=-Atualização de Dados-=-")

  nomebusca = input("Nome Atual: ")

  if nomebusca == "0":
    print("\n\t-=-Atualização Cancelada-=-")
    exit()

  if nomebusca in vetNomes:
      local = vetNomes.index(nomebusca)
      vetNomes[local] = lerNome(vetNomes)
      vetTelefones[local] = lerTelefone(vetTelefones)
      print("\n\t-=- Atualização Concluida -=-\n")

  salvar(vetNomes, "nomes.json")
  salvar(vetTelefones, "telefones.json")

def removerCadastro(vetNomes,vetTelefones):
  print("\n\t-=-Remoção de Cadastro-=-")

  nomebusca = input("Nome Atual: ")

  if nomebusca == "0":
    print("\n\t-=-Atualização Cancelada-=-")
    exit()

  if nomebusca in vetNomes:
    local = vetNomes.index(nomebusca)

    vetNomes.pop(local)
    vetTelefones.pop(local)
    salvar(vetNomes, "nomes.json")
    salvar(vetTelefones, "telefones.json")

    print("\n\t-=-Cadastro Removido-=-")

def buscarLetra(vetNomes,vetTelefones):
  print("\n\t-=-Busca por Letra-=-\n")

  i = 0
  letra = input("Letra: ")
  print("\n\t-=- Buscando -=-\n")
  while letra.isalpha() != True or len(letra) != 1:
    letra = input("\n\t-=-Valor Digitado Invalido-=-\nLetra: ")

  while i < len(vetNomes):
    if vetNomes [i][0] == letra or vetNomes[i][0] == letra.upper():
      print(vetNomes[i] , " - " , vetTelefones[i])
    i = i + 1

  print("\n\t-=- Fim da Busca -=-")

def menu():
  print("\n\t-=- Menu -=-")
  print("Digite 0 para encerrar o programa")
  print("Digite 1 para cadastrar")
  print("Digite 2 para imprimir")
  print("Digite 3 para buscar por letra")
  print("Digite 4 para atualizar cadastro")
  print("Digite 5 para remover cadastro\n")

def op():
  op = input("Digito: ")
  while op.isdigit() != True or int(op) < 0 or int(op) > 5:
    op = input("\n\t-=-Valor Digitado Invalido-=-\nDigito: ")
  return int(op)

def main():
  # Variaveis Iniciais
  vetNomes = carregar("nomes.json")
  vetTelefones = carregar("telefones.json")
  print("\n\t-=-AGENDA TELEFÔNICA-=-")
  menu()
  op_ = op()

  while op_ != 0:

    if op_ == 1:

      print("\n\t-=- Cadastro -=-\n")

      cadastroNome(vetNomes)
      cadastroTelefone(vetTelefones)

      print("\n\t-=- Cadastro Concluido -=-")

      menu()
      op_ = op()

    if op_ == 2:

      listaContatos(vetNomes,vetTelefones)
      menu()
      op_ = op()

    if op_ == 3:

      buscarLetra(vetNomes,vetTelefones)
      menu()
      op_ = op()

    if op_ == 4:

      atualizarCadastro(vetNomes,vetTelefones)
      menu()
      op_ = op()

    if op_ == 5:

      removerCadastro(vetNomes,vetTelefones)
      menu()
      op_ = op()

  print("\n\t-=- Programa Encerrado -=-")

main()
