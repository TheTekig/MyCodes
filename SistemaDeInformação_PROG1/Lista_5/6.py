def somaImposto():
  taxaImposto = input("Taxa do Imposto --->")
  while taxaImposto.replace(".","").isdigit() != True or float(taxaImposto) <0:
    taxaImposto = input("\n\t-=-Valor Digitado Invalido-=-\nTaxa do Imposto ---> ")

  taxaImposto = float(taxaImposto) / 100

  valorCusto = input("Valor de Custo --->")
  while valorCusto.replace(".","").isdigit() != True or float(valorCusto) <0:
    valorCusto = input("\n\t-=-Valor Digitado Invalido-=-\nValor de Custo ---> ")

  Val_com_imposto = (float(valorCusto) * taxaImposto) + float(valorCusto)

  return Val_com_imposto

#Inicio do Programa
somaImposto()