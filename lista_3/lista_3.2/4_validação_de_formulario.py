#Entrada e Validacao de Dados

def nome():
    name = str(input("Nome --> "))
    while len(name) < 3:
        print("Nome Invalido")
        name = str(input("Nome --> "))
    return(name)

def age():
    idade = int(input("Idade -->"))
    while idade < 0 or idade > 150:
        print("Idade Invalida")
        idade = int(input("Idade -->"))
    return(idade)

def payment():
    salario = float(input("Salario -->"))
    while salario < 0:
        print("Salario Invalido")
        salario = float(input("Salario -->"))
    return(salario)

def gender():
    sexo = str(input("Digite `f` para Feminino e `m` para Masculino -->"))
    while sexo != "f"  and sexo != "m" :
        print("Sexo Invalido")
        sexo = str(input("Digite `f` para Feminino e `m` para Masculino -->"))
    return(sexo)

i1 = nome()
i2 = age()
i3 = payment()
i4 = gender()

print("\nNome:%s\nIdade:%d\nSalario:%.2f\nSexo:%s" %(i1,i2,i3,i4))
