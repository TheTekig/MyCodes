
#Testando se a nota e valida
def testando_nota():
    n = float(input("Primeira Nota -->"))
    while n < 0: 
        print("Nota Invalida")
        n = float(input("Primeira Nota -->"))
    return (n)
#Print da Media
def median():
    media = (n1 + n2 + n3) / 3
    if media < 6:
        print("%s Reprovado\nMédia ---> %.2f" %(name,media))

    elif media >= 7:
        print("%s Aprovado\nMédia ---> %.2f" %(name,media))

    else:
        print("%s Prova Final\nMédia ---> %.2f" %(name,media))
#Execução do Programa
name = str(input("Digite Seu Nome --->"))

n1 = testando_nota()
n2 = testando_nota()
n3 = testando_nota()

if n1 > n2 or n1 > n3:
    pos1 = n1
    if n2 > n3:
        pos2 = n2
        pos3 = n3
    else:
        pos3 = n2
        pos2 = n3

elif n2 > n1 or n2 > n3:
    pos1 = n2
    if n1 > n3:
        pos2 = n1
        pos3 = n3
    else:
        pos2 = n3
        pos3 = n1


elif n3 > n2 or n3 > n1:
    pos1 = n3
    if n2 > n1:
        pos2 = n2
        pos3 = n1
    else:
        pos3 = n1
        pos2 = n2

else:
    pos1 = n1
    pos2 = n2
    pos3 = n3

median()

print("Suas Notas foram %.2f, %.2f e %.2f" %(pos1 , pos2, pos3))


