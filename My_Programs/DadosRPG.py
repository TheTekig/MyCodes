import random

def rolar_dadod3():
  dado = random.randint(1,3)
  return dado
def rolar_dadod6():
  dado = random.randint(1,6)
  return dado
def rolar_dadod20():
  dado = random.randint(1,20)
  return dado
def rolar_dadod100():
  dado = random.randint(1,100)
  return dado
def qtd_dados():
  qtd = input("Digite a quantidade de dados que deseja rolar: ")
  while qtd.isnumeric() == False or int(qtd) < 1:
    print("A quantidade deve ser um número e maior ou igual a 1.")
    qtd = input("Digite a quantidade de dados que deseja rolar: ")
  return int(qtd)

def menu_():
  print("\n\t-=-Sistema de Dado-=-")
  print("\n1 - 1D3")
  print("2 - 1D6")
  print("3 - 1D20")
  print("4 - 1D100")
  print("5 - Sair\n")

  opcoes = input("Digite a opção desejada: ")

  while opcoes.isnumeric() == False or int(opcoes) < 1 or int(opcoes) > 5:
    print("A opção deve ser um número e estar entre 1 e 5.")
    opcoes = input("Digite a opção desejada: ")

  D3 = rolar_dadod3()
  D6 = rolar_dadod6()
  D20 = rolar_dadod20()
  D100 = rolar_dadod100()


  if opcoes == "1":
    qtd = qtd_dados()
    valtotal_dados = D3 * qtd
    print("O valor total dos dados é: ", valtotal_dados)
    menu_()
  elif opcoes == "2":
    qtd = qtd_dados()
    valtotal_dados = D6 * qtd
    print("O valor total dos dados é: ", valtotal_dados)
    menu_()
  elif opcoes == "3":
    qtd = qtd_dados()
    valtotal_dados = D20 * qtd
    print("O valor total dos dados é: ", valtotal_dados)
    menu_()
  elif opcoes == "4":
    qtd = qtd_dados()
    valtotal_dados = D100 * qtd
    print("O valor total dos dados é: ", valtotal_dados)
    menu_()
  else:
    print("Saindo...")
    exit()

def main():
  menu_()

main()

