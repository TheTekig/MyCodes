
#Funcoes
def ler_nome(qtname):
    name = input("\nName %d --->" %qtname)
    while name.replace(" ","").isalpha() != True or len(name) < 0:
         name = input("\t-=- Invalid Name -=-\nName %d --->" %qtname)
    return name
def ler_gabarito(qtd):
    gabarito = input("Question %d ---> " %qtd)
    while gabarito.isalpha() != True or gabarito.lower() != "a" and gabarito.lower() != "b" and gabarito.lower() != "c" and gabarito.lower() != "d" and gabarito.lower() != "e":
        gabarito = input("\t-=- Invalid Answer -=-\nQuestion %d ---> " %qtd)
    return gabarito

print("\n\t-=- Definindo Gabarito -=-")
#Definindo Gabarito
question1 = ler_gabarito(1)
question2 = ler_gabarito(2)
question3 = ler_gabarito(3)
question4 = ler_gabarito(4)
question5 = ler_gabarito(5)
question6 = ler_gabarito(6)
question7 = ler_gabarito(7)
question8 = ler_gabarito(8)
question9 = ler_gabarito(9)
question10 = ler_gabarito(10)

#Declarando algumas Variaveis
qtname = 0
pts  = 0
totalpontos = 0
maiornota = -999
menornota = 999

#Entrada De Respostas
print("\n\t-=- Fill Your Answers -=-")

#Definindo chamado
continuar = "S"

while continuar.upper() == "S":

    #Nome e Quantidade de Usuarios
    qtname = qtname + 1
    nome = ler_nome(qtname)

    #Entrada de Respostas
    answer1 = ler_gabarito(1)
    if answer1 == question1:
        pts = pts + 1
    answer2 = ler_gabarito(2)
    if answer2 == question2:
        pts = pts + 1
    answer3 = ler_gabarito(3)
    if answer3 == question3:
        pts = pts + 1
    answer4 = ler_gabarito(4)
    if answer4 == question4:
        pts = pts + 1
    answer5 = ler_gabarito(5)
    if answer5 == question5:
        pts = pts + 1
    answer6 = ler_gabarito(6)
    if answer6 == question6:
        pts = pts + 1
    answer7 = ler_gabarito(7)
    if answer7 == question7:
        pts = pts + 1
    answer8 = ler_gabarito(8)
    if answer8 == question8:
        pts = pts + 1
    answer9 = ler_gabarito(9)
    if answer9 == question9:
        pts = pts + 1
    answer10 = ler_gabarito(10)
    if answer10 == question10:
        pts = pts + 1

    #Quantidade de Acertos
    print("Score ---> %d" %pts)

    #Maior e Menor Nota
    if pts >= maiornota:
        maiornota = pts
        maiornome = nome

    if pts <= menornota:
        menornota = pts
        menornome = nome

    #Total de Pontos
    totalpontos = totalpontos + pts
    pts = 0
    
    #Menu
    continuar = input("Press 'S' To continue and 'N' to Stop ---> ")
    while continuar.isalpha() != True or continuar.upper() != "S" and continuar.upper() != "N":
        continuar = input("-=- Invalid Entry -=-\nPress 'S' To Continue and 'N' to Stop ---> ")

#Media de Notas dos Alunos
media = totalpontos / qtname

print("\n\t-=- Stats -=-\n\nStudent %s has the higher Grade ---> %d \t Student %s has the lower grade ---> %d\nQuantity of Students used ---> %d \t Media of Students grade ---> %d\n" %(maiornome,maiornota,menornome,menornota,qtname,media))




