usuarios = 0
maiorpts = -999
menorpts = 999

def ler_aluno():
    aluno = input("Nome Aluno ---> ")

    while aluno.isalpha() != True or len(aluno) > 20:
        aluno = input("\t-=- Resposta Invalida -=-\nNome Aluno  ---> " )

    return aluno

def ler_nota():
    nota = input("Questao ---> " )

    while nota.isalpha() != True or nota != "a" and nota != "b" and nota != "c" and nota != "d" and nota != "e":
        nota = input("\t-=- Resposta Invalida -=-\nQuestao  ---> ")

    

    return nota

def continuar_():
    continuar = input("Digite s/n ---> ")
    while continuar.isalpha() != True or continuar != "s" and continuar != "n":
        continuar = input("\t-=- Valor Invalido -=-\nDigite s/n ---> ")
    return continuar

#Gabarito
questao1 = "a"
questao2 = "b"
questao3 = "c"
questao4 = "d"
questao5 = "e"
questao6 = "e"
questao7 = "d"
questao8 = "c"
questao9 = "b"
questao10 = "a"

continuar = "s"

while continuar == "s":

    pts = 0

    nome = ler_aluno()

    answer1 = ler_nota()
    if questao1 == answer1:
        pts = pts + 1

    answer2 = ler_nota()
    if questao2 == answer2:
        pts = pts + 1

    answer3 = ler_nota()
    if questao3 == answer3:
        pts = pts + 1

    answer4 = ler_nota()
    if questao4 == answer4:
        pts = pts + 1

    answer5 = ler_nota()
    if questao5 == answer5:
        pts = pts + 1

    answer6 = ler_nota()
    if questao6 == answer6:
        pts = pts + 1

    answer7 = ler_nota()
    if questao7 == answer7:
        pts = pts + 1

    answer8 = ler_nota()
    if questao8 == answer8:
        pts = pts + 1

    answer9 = ler_nota()
    if questao9 == answer9:
        pts = pts + 1

    answer10 = ler_nota()
    if questao10 == answer10:
        pts = pts + 1

    print("Quantidade de Acertos ---> %d" %pts)
    

    if pts > maiorpts:
        maiorpts = pts
        maiornome = nome


    if pts < menorpts:
        menorpts = pts
        menornome = nome


    usuarios  = usuarios + 1

    soma = (pts + pts) 

    continuar = continuar_()

media = soma / usuarios

print("Aluno %s Maior Nota ---> %d\tAluno %s Menor Nota ---> %d\n\tQuantidade de Usuarios ---> %d \tMedia Notas ---> %.2f " %(maiornome,maiorpts,menornome,menorpts,usuarios,media))
    
    

