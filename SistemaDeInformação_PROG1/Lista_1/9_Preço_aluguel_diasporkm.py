print("\nVamos calcular o preço a pagar por um carro alugado com base na Quilometragem marcada e no dia que esta em posse!!!\n")
#Banco de Dados
dias = float(input("Dias de utilização do carro:"))
km   = float(input("Quantidade de KM rodados:"))
alpd = 60.00
kmr  = 0.15 
#Calculos
diap = dias * alpd
kmp = km * kmr
totalp = diap + kmp
#Resultado
print("\nO valor total por essa quantidade de KM e dias usados é de $%.2f" %(totalp))
