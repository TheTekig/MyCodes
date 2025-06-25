def produto_():
    produto = float(input("\nValor Do Produto ---> $"))
    while produto < 0:
        produto = float(input("Valor Invalido\nValor Do Produto ---> $"))
    return(produto)

def soma_produto_():
    produto1 = produto_()
    produto2 = produto_()
    produto3 = produto_()

    total_ = produto1 + produto2 + produto3
    print("\nTotal dos Produtos ---> $%.2f" %total_)
    return(total_)

def dinheiro_():
    dinheiro = float(input("\nDinheiro ---> $"))
    while dinheiro < 0:
        dinheiro = float(input("Valor Invalido\nValor entregado ---> $"))
    return(dinheiro)

def troco():
    total_  = soma_produto_()
    valor_  = dinheiro_()

    troco = total_ - valor_

    while valor_ < total_:
        print("Faltam $%.2f" %(troco))
        valor_ = dinheiro_()
        troco = (total_ - valor_) 
        troco = troco * -1

    print(f"Troco ---> ${troco} \n")

def menu_():

    troco()
    print("=====Compra Finalizada=====\n\n=====Compra Iniciada=====")
    menu_()

print("\n=====INICIALIZANDO=====\n")
menu_()


    









        
