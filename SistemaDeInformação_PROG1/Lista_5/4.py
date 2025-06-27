def Limite():
  limite = input("Limite ---> ")
  while limite.isdigit() != True or int(limite) < 0:
    limite = input("Limite ---> ")
  return int(limite)
def imprimir(limite):

  cont = 1
  while cont <= limite:

    collum = 1
    result = ""

    while collum <= cont:
      result = result + str(collum) + " "
      collum = collum + 1
    print(result)
    cont = cont + 1
def menu():
  limite = Limite()
  imprimir(limite)

#Inicio do Programa
menu()