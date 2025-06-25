
x = 1

altura_total = 0

name = str(input("Nome -->"))

lenght = float(input("Altura -->"))

while lenght < 0:
    lenght = float(input("Altura invalida, Digite Novamente-->"))

nomenor = name
menor = lenght
nomaior = name
maior = lenght

while x != 20:

    name = str(input("Nome -->"))

    lenght = float(input("Altura -->"))

    while lenght < 0:
        lenght = float(input("Altura invalida, Digite Novamente-->"))

  
    if lenght <= lenght:
        nomenor = name
        menor = lenght

    elif lenght >= lenght:
        nomaior = name
        maior = lenght


    
    altura_total = altura_total + lenght
    x = x + 1
    


media = altura_total  / 20

print(f"\nmedia total ---> {media}\nmenor altura ---> {nomenor} / {menor}\nmaior altura ---> {nomaior} {maior}")



