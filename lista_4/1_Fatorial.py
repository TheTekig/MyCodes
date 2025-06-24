print("Vamos Calcular o fatorial de um número")
num = float(input("Digite o número ---> "))
fatorial = 1
numprint = num
while num != 1:

    fatorial = fatorial * num
    num = num - 1

print (f"Fatorial --> {fatorial}\nNúmero --> {numprint}")