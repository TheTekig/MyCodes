print("Vamos calcular o tempo de vida que um fumante perde com base nos cigarros tragados")
#Entrada de Dados
cig_f = int(input("Quantidade de Cigarros tragados por dia:"))
anos_f = int(input("Quantidade de anos que fuma:"))
#Calculos
min = 10
tvp = cig_f * min #tempo de vida perdido
dias = anos_f * 365
totalp = (dias * tvp) / 1440

#Resultado
print("A quantidade de dias perdidos por fumar é de %d dias" %(totalp))
