
qtd = 1

def ler_nota(qtd):
    nota = input("Nota %d ---> " %qtd)
    nota = float(nota)
    while nota.replace("." , "").isdigit() != True or nota < 0 or nota > 100:
        nota = input("\t-=-Número Digitado Inválido-=-\nNota %d ---> " %qtd)
    qtd = qtd + 1
    
    return nota

def calculo_media(n1,n2,n3):
    media = (n1 + n2 + n3) / qtd

    return media

n1 = ler_nota()
n2 = ler_nota()
n3 = ler_nota()

calculo_media()

if n1 > n2 and n1 > n3:
    if n2 > n3:
        n1,n2,n3 = n1,n2,n3       
    else:      
        n1,n3,n2 = n1,n2,n3

elif n2 > n3:
    if n3 > n1:
        n2,n3,n1 = n1,n2,n3
    else :
        n2,n1,n3 = n1,n2,n3

elif n3 > n2:
    if n2 > n1:
        n3,n2,n1 = n1,n2,n3

