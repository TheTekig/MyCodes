def entrada_codigo():

    num = (input("Digito --->"))
    
    while num.isdigit() == False or (int(num) < 0):
        num = (input("Entrada Invalida Digite Novamente\nDigito --->"))
   
    return int(num)

def entrada_altura():

    num = (input("Digito --->"))
    
    while num.replace(".","").isdigit() == False or (float(num) < 0) or (float(num) > 2.5):
        num = (input("Entrada Invalida Digite Novamente\nDigito --->"))
   
    return float(num)

def entrada_peso():

    num = (input("Digito --->"))
    
    while num.replace(".","").isdigit() == False or (float(num) < 0) or (float(num) > 500):
        num = (input("Entrada Invalida Digite Novamente\nDigito --->"))
   
    return float(num)

def menu_():

    num = (input("Aperte qualquer numero positivo Para proseguir e '0' para Parar\nDigito --->"))
    
    while num.isdigit() == False or (int(num) < 0):
        num = (input("Entrada Invalida Digite Novamente\nDigito --->"))
   
    return int(num)

menu = menu_()


altura_up = -9999
altura_down = 9999
peso_up = -9999
peso_down = 9999

if menu != 0:
    while menu != 0:

        print("\nDigite seu Código")
        codigo = entrada_codigo()
        print("Digite sua Altura")
        altura = entrada_altura()
        print("Digite seu Peso")
        peso   = entrada_peso()

        #Comparações

        if altura_up <= altura:
            if altura_up >= altura_up:
                altura_up = altura
                codigo_1 = codigo

        elif altura_down >= altura:
            altura_down = altura
            if altura_down <= altura_down:
                altura_down = altura
                codigo_2 = codigo

        if peso_up <= peso:
            if peso_up >= peso_up:
                peso_up = peso
                codigo_3 = codigo

        elif peso_down >= peso:
            peso_down = peso
            if peso_down <= peso_down:
                peso_down = peso
                codigo_4 = codigo

        menu = menu_()
    print("O Código mais pesado ---> %d Peso ---> %.2f\nO Código mais Leve ---> %d Peso ---> %.2f\nO Código mais Alto ---> %d Altura ---> %.2f\nO Código mais Baixo ---> %d Altura ---> %.2f" %(codigo_3,peso_up,codigo_4,peso_down,codigo_1,altura_up,codigo_2,altura_down))
    print("Programa Encerrado")

else:
    print("Programa Encerrado")