num = int(input("Digite um número entre 0 e 10 ---> "))

while num < 0 or num > 10:
    print("Número Invalido")
    num = int(input("Digite um número entre 0 e 10 ---> "))

print(f"blablabla {num}")