print("Vamos calcular o valor do desconto do produto!!!\n")
#Entrada de Dados
produto = str(input("Nome do Produto:"))
preco   = float(input("Preço do Produto:"))
quantidade = int(input("Quantidade do produto:"))
desconto= float(input("Valor do Desconto:"))
#Calculo de Desconto e Valor Total
desconto = (desconto / 100) * preco
preco = preco - desconto
valtotal = preco * float(quantidade)

#Resultado
print("\nO valor do produto %s em unidade com desconto é de $%.2f \n O valor total da compra com desconto é igual a %.2f " %(produto, preco, valtotal))

