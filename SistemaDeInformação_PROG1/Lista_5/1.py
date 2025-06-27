def nome_aluno():
    aluno = input("\nNome Estudante ---> ")
    while aluno.replace(" ","").isalpha() != True or len(aluno) < 0:
        aluno = input("\n\t-=-Entrada Invalida-=-\nNome Estudante ---> ")
    return aluno

def nota_aluno(qtd):
    nota = input("Nota %d ---> " %qtd)
    while nota.isdigit() != True or float(nota) < 0 or float(nota) > 10:
        nota = input("\t-=-Valor Invalido-=-\nNota %d ---> " %qtd)
    return nota

#Iniciar
print("\n\t-=- Sistema Média Trimestre -=-")

continue_ = "S"

while continue_.upper() == "S":
    #Definindo Variaveis
    menornota = 999
    maiornota = -999
    media = 0

    #Nome do Aluno
    nome = nome_aluno()

    #Notas do Aluno
    nota1 = float(nota_aluno(1))
    nota2 = float(nota_aluno(2))
    nota3 = float(nota_aluno(3))

    total = nota1 + nota2 + nota3
    media = total / 3

    if nota1 >= nota2 and nota1 >= nota3:
        if nota2 >= nota3:
            nota1,nota2,nota3 = nota1,nota2,nota3
        else:
            nota1,nota3,nota2 = nota1,nota2,nota3
    elif nota2 >= nota3:
        if nota3 >= nota1:
            nota2,nota3,nota1 = nota1,nota2,nota3
        else:
            nota2,nota1,nota3 = nota1,nota2,nota3
    else:
        if nota2 >= nota1:
            nota3,nota2,nota1 = nota1,nota2,nota3
        else:
            nota3,nota1,nota2 = nota1,nota2,nota3

    if media >= 7:
        print("O Estudante %s foi Aprovado com a média ---> %.2f \tTotal de Pontos ---> %d\tNotas em Ordem Decrescente ---> %.2f - %.2f - %.2f " %(nome,media,total,nota1,nota2,nota3))
    elif media > 6:
        print("O Estudante %s esta na Prova Final com a média ---> %.2f \tTotal de Pontos ---> %d\tNotas em Ordem Decrescente ---> %.2f - %.2f - %.2f " %(nome,media,total,nota1,nota2,nota3))
    else:
        print("O Estudante %s foi Reprovado com a média ---> %.2f \tTotal de Pontos ---> %d\tNotas em Ordem Decrescente ---> %.2f - %.2f - %.2f " %(nome,media,total,nota1,nota2,nota3))
    
    continue_ = input("\nDeseja Iniciar com outro Usuario?(S/N) ---> ")
    while continue_.isalpha() != True or continue_.upper() != "S" and continue_.upper() != "N":
        continue_ = input("\t-=-Entrada Invalida-=-\nDeseja Iniciar com outro Usuario?(S/N) ---> ")

print("\n\t-=- Sessão Finalizada -=-\n")

