import math

m2 = float(input("\nBem-Vindo a 'Bendita Tinta' sua loja de Tinta!!!\nPara melhor auxilialo treinamos nosso sistema para te dar uma estimativa do valor que sera gasto por metro quadrado e a quantidade de latas que serão utilizadas para o senhor!!!\nInsira o a quantidade de metro quadrados ao lado ----> "))
vtinta = 80.00
litros = m2/3
lata = litros/18
vlata = lata * vtinta
lata = math.ceil(lata)
valtotal = lata * vtinta

print("\nFizemos os calculos para você!!!\nVocê necessitara de %d Latas\nO Valor individual de cada lata é %.2f\nO Valor total por todas as latas que ira necessitar é de %.2f\nObrigado pela sua preferência!!! :)" %(lata,vtinta,valtotal))
