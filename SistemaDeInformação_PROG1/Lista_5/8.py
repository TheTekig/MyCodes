def valorPagamento(val_prestacao,d_atraso):
  if d_atraso == 0:
    val_prestacao = float(val_prestacao)
  else:
    val_prestacao = float(val_prestacao) + (float(val_prestacao) * 0.03) + (float(val_prestacao) * 0.001 * int(d_atraso))


  return val_prestacao
def relatorio(val_prestacao,d_atraso,valfinal,valortotal):

    valortotal = valorPagamento(val_prestacao,d_atraso)
    valfinal = valfinal + valortotal

    return valfinal
def menu():
  print("\n   -=- Programa de Pagamento -=-")
  #Menu
  print("\n\t   -=- Menu -=-")
  print("Digite 0 para encerrar o programa")

  #Contador de Usuarios
  cont = 0

  #Variaveis Iniciais
  valortotal = 0
  valfinal = 0
  val_prestacao = 1

  #Inicio Loop Principal
  while val_prestacao != 0:

    #Lendo Valor da Prestação
    print("\n\t-=- Prestação -=-")
    val_prestacao = input("Valor da Prestação (BRL$) ---> ")

    #Definindo limites da prestação
    while val_prestacao.replace(".","").isdigit() != True or float(val_prestacao) < 0:
      val_prestacao = input("\n\t-=-Valor Digitado Invalido-=-\nValor da Prestação (BRL$) ---> ")

    #Condicional para continuar o Loop ou Interrompelo
    if val_prestacao == "0":
      break
    else:

      #Lendo Dias de Atraso
      print("\n\t-=- Dias de Atraso -=-")
      d_atraso = input("Dias de Atraso ---> ")

      #Definindo limites dias de Atraso
      while d_atraso.isdigit() != True or int(d_atraso) < 0:
        d_atraso = input("\n\t-=-Valor Digitado Invalido-=-\nDias de Atraso ---> ")

      #Funcao que vai Calcular com base no valor do atraso e multas o valor do pagamento

      valfinal = relatorio(val_prestacao,d_atraso,valfinal,valortotal)
      cont = cont + 1

  #Print do Relatório do Dia
  print("\n\t-=- Relatório -=-\nValor Total de Prestações Pagas ---> %.2f\nQuantidade de Transações feitas ---> %.0f" %(valfinal,cont))

#Inicio do Programa
menu()