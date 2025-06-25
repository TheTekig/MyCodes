print("Escreva dois numeros para serem somados")
num1 = int(input("escreva o primeiro numero:"))
num2 = int(input("escreva o segundo numero:"))

soma = num1 + num2
resto = 2%soma

if (resto == 0):
    print("A soma de %d e %d é igual a %d , este numero é par" %(num1 , num2 , soma))

else:
     print("A soma de %d e %d é igual a %d , este numero é impar" %(num1 , num2 , soma))

