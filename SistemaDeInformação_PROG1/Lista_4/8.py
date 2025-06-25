print("\n\t-=-Calculador de Consumo-=-\n")

def numero_consumidor():
    num = input("Numero Consumidor ---> ")

    while num.isdigit() != True or int(num) < 0:
        num = input("Numero Invalido - Tente Novamente\nNumero Consumidor ---> ")
    return int(num)

def qnt_kwh():
    num = input("Quantidade kWh Consumidas ---> ")
    while num.replace(".","").isdigit() != True or float(num) < 0:
        num = input("Numero Invalido - Tente Novamente\nQuantidade kWh Consumidas ---> ")
    return float(num)

def codigo():
    num = input("\n\t-=-Preencha Tipo de Consumidor-=-\n\n\t\t1 - Residencial\n\t\t2 - Comercial\n\t\t3 - Industrial\n\nConsumidor ---> ")
    while num.isdigit() != True or (int(num) < 1) or (int(num) > 3):
        num = input("Numero Invalido - Tente Novamente\nCodigo Consumidor ---> ")
    return int(num)

residencial = 0.3
comercial = 0.5
industrial = 0.7


re_total = 0
co_total = 0
in_total = 0

nc = numero_consumidor()

if nc != 0:
    while nc != 0:

        qk = qnt_kwh()
        c  = codigo()

        if c == 1:
            re_total = qk * residencial
            print("\nConsumidor ---> %d\tCodigo ---> %d\nValor Residencial Total ---> $%.2f\n" %(nc,c,re_total))
        elif c == 2:
            co_total = qk * comercial
            print("\nConsumidor ---> %d\tCodigo ---> %d\nValor Comercial Total ---> $%.2f\n" %(nc,c,co_total))
        else:
            in_total = qk * industrial
            print("\nConsumidor ---> %d\tCodigo ---> %d\nValor Industrial Total ---> $%.2f\n" %(nc,c,in_total))

        media = (re_total + co_total) / 2 

        nc = numero_consumidor()



    print("\n\t=-= Consumo dos Tipos de Consumidores =-=\nResidencial ---> %.2f\tComercial ---> %.2f\tIndustrial ---> %.2f\n\nMédia de Consumo do Residencial e Comercial ---> %.2f " %(re_total,co_total,in_total,media))
    print("\n\n\t-=- Programa Encerrado -=-")

else:
    print("\n\t\t-=- Programa Encerrado -=-")





