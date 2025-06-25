#Entrada de Variaveis
idade = int(input("\nIdade ---> "))
peso = float(input("\nPeso ---> " ))
mg = 0

#Processamento
if idade >= 12:

    if peso > 60:
        mg = 1000


    else:
        mg = 875

else:

    if peso < 5: 
        print("Você Esta Vivo?")
    elif peso < 9:
        mg = 125
    elif peso < 16:
        mg = 250
    elif peso < 24:
        mg = 375
    elif peso < 30:
        mg = 500
    else:
        mg = 750

gotas = mg / 25

#Saida

print("\n\nIdade ----> %d Anos\tPeso ----> %.1fKG\nDosagem ---->%dmg\tGotas ----> %dGotas\n\n" %(idade,peso,mg,gotas))