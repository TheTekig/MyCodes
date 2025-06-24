#Entrada de Dados
name = str(input("Digite Seu Nome --->"))

#Testando se a nota e valida
n1 = float(input("Primeira Nota -->"))
while n1 < 0: 
    print("Nota Invalida")
    n1 = float(input("Primeira Nota -->"))

n2 = float(input("Segunda Nota -->"))
while n2 < 0: 
    print("Nota Invalida")
    n2 = float(input("Segunda Nota -->"))

n3 = float(input("Terceira Nota -->"))
while n3 < 0: 
    print("Nota Invalida")
    n3 = float(input("Terceira Nota -->"))

media = (n1 + n2 + n3) / 3
#Posicao em ordem decrescente
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

#Print da Media
if media < 6:
    print("%s Reprovado" %name)

elif media >= 7:
    print("%s Aprovado" %name)

else:
    print("%s Prova Final" %name)

#Print das Notas
print("Suas Notas foram %.2f, %.2f e %.2f" %(pos1,pos2,pos3))