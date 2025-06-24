nota = int(input("\nDigite sua nota sabendo que a maxima é 10 e a minima é 0 :"))

while nota < 0 or nota > 10:
    nota = int(input("\nNota invalida, digite novamente: "))    

print("Sua nota é %d" %nota)