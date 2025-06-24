print("\nDigite sua nota sabendo que a maxima é 10 e a minima é 0!\n")

nota1 = int(input("Primeira Nota: "))
while nota1 < 0 or nota1 > 10:
    nota1 = int(input("\nNota invalida, digite novamente: "))

nota2 = int(input("Segunda Nota: "))
while nota2 < 0 or nota2 > 10:
    nota2 = int(input("\nNota invalida, digite novamente: ")) 

nota3 = int(input("Terceira Nota: "))
while nota3 < 0 or nota3 > 10:
    nota3 = int(input("\nNota invalida, digite novamente: "))  
    
media = float(nota3 + nota2 + nota1) / 3

if media < 6:
    print("\nSua média é %0.2f, você reprovou!!!" %media)
elif media >= 7:
    print("\nSua média é %0.2f, você passou!!!" %media)
else:
    print("\nSua média é %0.2f, você recuperação!!!" %media)