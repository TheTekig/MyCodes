
print("\nEscreva uma quantidade de Dias,Horas,Minutos e Segundos e converterei tudo para segundos!!!\n")

dias = float(input("Dias:"))
horas = float(input("Horas:"))
minutos = float(input("Minutos:"))
segundos = float(input("Segundos:"))

dph = dias * 24
hpm = (dph + horas) * 60
mps = (hpm + minutos) * 60
seg = mps + segundos

print("\nO total em segundos do tempo que você colocou é %.1f\n" %(seg))




