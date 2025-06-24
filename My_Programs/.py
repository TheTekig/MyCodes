
print("Escreva 3 numeros e eu direi qual o maior e o menor e os colocarei em ordem crescente!!!")
#Entrada De Dados
num1    = float(input("Primeiro numero: "))
num2    = float(input("Segundo numero: "))
num3    = float(input("Terceiro numero: "))

if (num1 > num2 and num1 > num3):
    position1 = num1
    if (num2 > num3):
        position2 = num2
        position3 = num3
    else:
        position2 = num3
        position3 = num2


if (num2 > num1 and num2 > num3):
    position1 = num2
    if (num1 > num3):
        position2 = num1
        position3 = num3
    else:
        position2 = num3
        position3 = num1

if (num3 > num1 and num3 > num2):
    position1 = num3
    if (num1 > num2):
        position2 = num1
        position3 = num2
    else:
        position2 = num2
        position3 = num1

print("O número %.2f é maior que o número %.2f, a organização em ordem crescente seria: %.2f , %.2f , %.2f" %(position1 , position2 , position3 , position2 , position1))

