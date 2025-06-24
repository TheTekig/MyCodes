
x = 1

altura_total = 0
maior = -999
menor = 999

while x != 21:

    name = str(input("Nome -->"))

    lenght = float(input("Altura -->"))

    while lenght < 0:
        lenght = float(input("Altura invalida, Digite Novamente-->"))

  
    if lenght < menor:
        menor = lenght

    if lenght > maior:
        maior = lenght
        

    altura_total = altura_total + lenght
    x = x + 1
    


media = altura_total  / 5

print(f"\nmedia total ---> {media}\nmenor altura ---> {menor}\nmaior altura ---> {maior}\n")



