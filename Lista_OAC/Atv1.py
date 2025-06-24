def entrada_dados():
    entry = input("Number ---> ")
    while entry.replace(".","").isdigit() != True:
        entry = input("Just Numbers Brow!\nNumber ---> ")
    
    return float(entry)

num1 = entrada_dados()
num2 = entrada_dados()

soma = num1 + num2

print(f"Soma é {soma}")





num = int(input("numero ="))
num3 = int(input("numero = "))

soma = num + num3

print(soma)