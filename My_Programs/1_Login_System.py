
login = []
password = []

def set_up():                                                                                                                           #REALIZA O CADASTRO DO USUARIO
    print("\n-=-SETUP-=-")
    print("\nSUA SENHA NÃO PODE CONTER: \n1.MESMO NOME DO USUARIO\n2.SER MENOR QUE 6 CARACTERES\n3.DIFERENÇA NA CONFIRMAÇÃO\n")
    user = str(input("USUARIO ---> "))
    pas = str(input("SENHA ---> "))
    conpas = str(input("CONFIRME A SENHA ---> "))
    while pas != conpas or len(pas) < 6 or user.upper() == pas.upper():
    
        print("\n-ERROR- Revise sua senha lembrando dos parametros citados anteriormente!\n")
        user = str(input("USUARIO ---> "))
        pas = str(input("SENHA ---> "))
        conpas = str(input("CONFIRME A SENHA ---> "))

    login.append(user)
    password.append(pas)
    print("\nSETUP FEITO COM SUCESSO!!!\n")

def log_in():                                                                                                                           #REALIZA O LOGIN DO USUARIO
    print("\n-=-LOGIN-=-")
    user = str(input("USUARIO ---> "))
    pas = str(input("SENHA ---> "))

    for i in range(len(login)):                                                                                                        #REALIZA UMA BUSCA NA LISTA PROCURANDO PELO USUARIO
        if login[i] == user and password[i] == pas:
            print(f"\nBEM-VINDO {login[i]}!\n")
            return
    print("\nFALHA AO COMPLETAR LOGIN!\n")    
    
def menu():                                                                                                                             #MENU DE OPÇÕES

    print("DIGITE '1' PARA LOG-IN\nDIGITE '2' PARA SETUP\nDIGITE '3' PARA SAIR")
    opcoes = int(input("\nDIGITO ---> "))

    if opcoes == 3:
            print("\nSAINDO DO SISTEMA...") 
    
    elif opcoes == 2:
            set_up()
            menu()

    elif opcoes == 1:
            log_in()
            menu()         
    else:       
             print("\nNÚMERO INVÁLIDO\n")
             menu()

       
print("\n=-=-=-TOUCH SYSTEMS-=-=-=\n")
menu()