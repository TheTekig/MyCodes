print("\nVamos calcular a média das suas duas ultimas notas!!!\n(OBS: A nota máxima de cada prova é 10)\n")

def entrada_de_dados():
    nota1 = float(input("Primeira Nota: "))
    nota2 = float(input("Segunda Nota: "))

    calculo(nota1,nota2)

def calculo(nota1,nota2):
    soma_das_notas = nota1 + nota2
    media = soma_das_notas/2
    comparacao(media)

def comparacao(media):  
    if (media < 7):
         print("sua média foi %0.2f, Reprovado" %(media))
    else:
         print("sua média foi %0.2f, Aprovado" %(media))
    if(media >= 10):
        print("sua média foi %0.2f, Aprovado com Distinção" %(media))


entrada_de_dados()