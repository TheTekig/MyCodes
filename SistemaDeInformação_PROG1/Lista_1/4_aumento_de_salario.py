print("Vamos calcular o aumento do salário!!!\n")
#Entrada de Dados
salario = float(input("Valor do Salário: ")) 
aumento = float(input("Porcentagem do aumento: ")) 
#Calculo
aumento = (aumento / 100) * salario 
salario = aumento + salario
#Resultado
print("O aumento foi de $%.2f tendo um salário agora de $%.2f" %(aumento , salario))