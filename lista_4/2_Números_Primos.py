num = int(input("Vamos Calcular se o seu número é primo ou não!\nDigite Seu Número ---> "))
cont = 0
cont2 = 0

while cont != num:
    cont = cont + 1
    div = num%cont
    

    if div == 0:
        print(cont)
        cont2 = cont2 + 1
      
if cont2 == 2:
    print("PRIMOOOOOOOOO!?")
else:
    print("NO ERESSS PRIMOOOOOOOO!?")
