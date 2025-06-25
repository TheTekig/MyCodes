itens = int(input("Quantidade de Itens --> "))
while itens < 1 or itens > 50:
    itens = int(input("Valor Invalido\nQuantidade de Itens --> "))

cont = 0

while cont < itens:

    valor = 1.99
    cont = cont + 1
    seq = valor * cont

    print("\nQtd\tValor\n %d\t$%.2f" %(cont,seq))
