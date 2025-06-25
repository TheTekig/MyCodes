
#Entrada do Código
codigo = int(input("Codigo ---> "))
while codigo > 40 or codigo < 1:
    codigo = int (input("-Código Invalido-\nCódigo ---> "))

qtd = int(input("Quantidade ---> "))
while qtd < 0:
    qtd = int(input("-Quantidade Invalida-\nQuantidade ---> "))

preco = 0

#Comparação de codigos

if codigo < 10:
    preco = 10

elif codigo < 20:
    preco = 15

elif codigo < 30:
    preco = 20

else:
    preco = 30

print("Valor do Produto UND ---> $%.2f" %preco)
#Calculos

valor = qtd * preco
print("Valor do Produto Total ---> $%.2f" %valor)

if valor < 250:
    valor = ( valor* -0.05) + valor
elif  valor > 500:
    valor = ( valor * -0.15) + valor
else:
    valor = ( valor * -0.1) + valor

print("Valor do Produto Com desconto aplicado ---> $%.2f" %valor)




