from io import open_code

def validar_nome():
  nome = input("Digite o nome do cliente: ")
  while  nome.replace(" ", "").isalpha() == False:
    print("O nome deve conter apenas letras.")
    nome = input("Digite o nome do cliente: ")
    if nome == 0:
      menu_()

  while nome in nomel:
    print("Cliente já cadastrado.")
    nome = input("Digite o nome do cliente: ")
    if nome == 0:
      menu_()

  return nome

def validar_cpf():
  cpf = input("Digite o CPF do cliente: ")
  while cpf.replace(".","").replace("-","").isnumeric() == False or len(cpf) != 11:
    print("O CPF deve conter apenas números e ter 11 dígitos.")
    cpf = input("Digite o CPF do cliente: ")
  while cpf in cpfl:
    print("CPF já cadastrado.")
    cpf = input("Digite o CPF do cliente: ")
  return cpf

def validar_email():
  email = input("Digite o email do cliente: ")
  while "@" not in email or "." not in email:
    print("O email deve conter um @ e um ponto.")
    email = input("Digite o email do cliente: ")
    while email in emaill:
        print("Email já cadastrado.")
        email = input("Digite o email do cliente: ")
  return email

def validar_idade():
  idade = input("Digite a idade do cliente: ")
  while idade.isnumeric() == False or int(idade) < 18:
    print("A idade deve ser um número e maior ou igual a 18.")
    idade = input("Digite a idade do cliente: ")
  return idade

def menu_():
  print("\n\t-=-Sistema de Cadastro de Clientes-=-")
  print("\n1 - Cadastrar cliente")
  print("2 - Listar clientes")
  print("3 - Atualizar cliente")
  print("4 - Excluir cliente")
  print("5 - Dados Cliente")
  print("6 - Sair\n")

  opcoes = input("Digite a opção desejada: ")
  while opcoes.isnumeric() == False or int(opcoes) < 1 or int(opcoes) > 6:
    print("A opção deve ser um número e estar entre 1 e 5.")
    opcoes = input("Digite a opção desejada: ")

  if opcoes == "1":

    print("\n\t-=-Cadastro de cliente-=-")
    nome = validar_nome()
    nomel.append(nome)

    cpf = validar_cpf()
    cpfl.append(cpf)

    email = validar_email()
    emaill.append(email)

    idade = validar_idade()
    idadel.append(idade)

    print("\n\tCliente cadastrado com sucesso!")
    menu_()

  if opcoes == "2":
    print("\n\t-=-Lista de clientes-=-\n")
    for i in nomel:
      print(i)
    menu_()

  if opcoes == "3":
    nome = input("Digite o nome do cliente que deseja atualizar: ")
    if nome == "0":
      menu_()

    while nome not in nomel:
      print("Cliente não encontrado.")
      nome = input("Digite o nome do cliente que deseja atualizar: ")
      if nome == "0":
        menu_()

    location = nomel.index(nome)

    print("\n\t-=-Atualização de cliente-=-")

    print("Nome Anterior: ",nomel[location])
    nomel[location] = validar_nome()
    print("CPF Anterior: ",cpfl[location])
    cpfl[location] = validar_cpf()
    print("Email Anterior: ",emaill[location])
    emaill[location] = validar_email()
    print("Idade Anterior: ",idadel[location])
    idadel[location] = validar_idade()
    print("\n\tCliente atualizado com sucesso!")
    menu_()

  if opcoes == "4":

    print("\n\t-=-Exclusão de cliente-=-\n")
    nome = input("Digite o nome do cliente que deseja Excluir: ")
    if nome == "0":
      menu_()

    while nome not in nomel:
      print("Cliente não encontrado.")
      nome = input("Digite o nome do cliente que deseja Excluir: ")
      if nome == "0":
        menu_()

    location = nomel.index(nome)

    nomel.pop(location)
    cpfl.pop(location)
    emaill.pop(location)
    idadel.pop(location)

    print("\n\tCliente excluido com sucesso!\n")
    menu_()

  if opcoes == "5":
    nome = input("Digite o nome do cliente que deseja ver os dados: ")
    if nome == "0":
      menu_()

    while nome not in nomel:
      print("Cliente não encontrado.")
      nome = input("Digite o nome do cliente que deseja ver os dados: ")

    location = nomel.index(nome)
    print("\n\t-=-Dados do cliente-=-\n")
    print("Nome: ", nomel[location])
    print("CPF: ", cpfl[location])
    print("Email: ", emaill[location])
    print("Idade: ", idadel[location])
    menu_()

  if opcoes == "6":
    print("Saindo...")
    exit()

nomel = []
cpfl = []
emaill = []
idadel = []

def main():
  menu_()

main()

