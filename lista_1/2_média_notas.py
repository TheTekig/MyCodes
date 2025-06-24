print("\nDigite as suas notas dos seus 4 bimestres e iremos te dar a média de suas notas\n")

quater1 = float(input("Digite sua nota do primeiro bimestre:"))
quater2 = float(input("Digite sua nota do segundo bimestre:"))
quater3 = float(input("Digite sua nota do terceiro bimestre:"))
quater4 = float(input("Digite sua nota do quarto bimestre:"))

soma = quater1 + quater2 + quater3 + quater4
media = soma/4

if (soma >= 60):
    
    print("\nSua nota total foi %.1f , com uma média de %.1f" %(soma,media))
    print("Parabéns você passou!!!\n")

if (soma < 60):

    print("\nSua nota total foi %.1f , com uma média de %.1f" %(soma,media))
    print("Infelizmente você não passou!!!\n")