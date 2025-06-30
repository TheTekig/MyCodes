def Limite():
  limite = input("Limite ---> ")
  while limite.isdigit() != True or int(limite) < 0:
    limite = input("Limite ---> ")
  return int(limite)
def imprimir(limite):

  cont = 0
  while cont <= limite:
    seguimento = cont
    print((str(cont) + " ") * cont)
    cont = cont + 1
def menu():
  limite = Limite()
  imprimir(limite)

#Inicio do Programa
menu()