def conversor(not24_h, not24_m):

  not24_h = int(not24_h)
  not24_m = int(not24_m)
  not12 = 0

  if not24_h < 12:
    not12_h = not24_h
    not12_m = not24_m
    not12 = str(not12_h) + ":" + str(not12_m).zfill(2) + " A.M."

  elif not24_h > 12:
    not12_h = not24_h % 12
    not12_m = not24_m
    not12 = str(not12_h) + ":" + str(not12_m).zfill(2) + " P.M."

  else:
    not12_h = not24_h
    not12_m = not24_m
    not12 = str(not12_h) + ":" + str(not12_m).zfill(2) + " P.M."

  return not12
def continuar():
  continuar = input("\n\t-=-Deseja Continuar? S/N-=-\n")
  while continuar.upper() != "S" and continuar.upper() != "N":
    continuar = input("\n\t-=-Valor Digitado Invalido-=-\nDeseja Continuar? S/N ---> ")

  return continuar
def menu():

  print("\t-=- Conversor de Horas -=-\n")
  continuar_ = "S"

  while continuar_.upper() == "S":

    not24_h = input("Hora ---> ")
    while not24_h.isdigit() != True or int(not24_h) < 0 or int(not24_h) > 23:
      not24_h = input("\n\t-=-Hora Invalida-=-\nHoras ---> ")

    not24_m = input("Minutos ---> ")
    while not24_m.isdigit() != True or int(not24_m) < 0 or int(not24_m) > 59:
      not24_m = input("\n\t-=-Minutos Invalido-=-\nMinutos ---> ")

    not24 = not24_h + ":" + not24_m.zfill(2)
    print("\nHorario Militar ---> %s" %not24)

    nota12 = conversor(not24_h, not24_m)
    print("Horario Civil ---> %s"   %nota12)

    continuar_ = continuar()

  print("\n\t-=- Programa Encerrado -=-")

#Inicio do Programa
menu()