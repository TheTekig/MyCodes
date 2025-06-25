#Entrada e Validacao de Dados
name = str(input("Nome --> "))
while len(name) < 3:
    print("Nome Invalido")
    name = str(input("Nome --> "))

idade = int(input("Idade -->"))
while idade < 0 or idade > 150:
    print("Idade Invalida")
    idade = int(input("Idade -->"))

salario = float(input("Salario -->"))
while salario < 0:
    print("Salario Invalido")
    salario = float(input("Salario -->"))

sexo = str(input("Digite `f` para Feminino e `m` para Masculino -->"))
while sexo != "f"  and sexo != "m" :
    print("Sexo Invalido")
    sexo = str(input("Digite `f` para Feminino e `m` para Masculino -->"))


print("Nome:%s\nIdade:%d\nSalario:%.2f\nSexo:%s" %(name,idade,salario,sexo))
