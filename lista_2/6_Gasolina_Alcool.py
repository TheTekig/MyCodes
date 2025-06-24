#Entrada_de_Dados
comb1 = str(input("Precione 'a' para Alcool e 'g' para gasolina: "))
#Comparações
if (comb1 == "a"):
    print("\nAlcool")
    litros = float(input("Quantidade de Litros: "))
    if (litros > 20):
        desconto = 5
    else:
        desconto = 3
    preco = 3.20                                        #Calculos_de_Desconto
    desconto = (desconto/100)*preco
    valt =(preco - desconto) * litros  
    comb1 = str("Alcool")
    print("O Valor da %s deu $%.2f " %(comb1,valt))
if (comb1 == "g"):
    print("\nGasolina")    
    litros = float(input("Quantidade de Litros: "))
    if (litros > 20):
        desconto = 6
    else:
        desconto = 4                                     #Calculos_de_Desconto
    preco = 3.90                                       
    desconto = (desconto/100)*preco
    valt = (preco - desconto) * litros
    comb1 = str("Gasolina")
    print("O Valor da %s deu $%.2f " %(comb1,valt))