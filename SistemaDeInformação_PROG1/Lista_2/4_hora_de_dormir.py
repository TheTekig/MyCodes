horario = int(input("Horario ---> "))

if horario < 5:
    print("Vai Dormir!")
elif horario < 12:
    print("Bom Dia!")
elif horario < 18:
    print("Boa Tarde!")
elif horario < 24:
    print("Boa Noite")
else:
    print("Horario Invalido!")