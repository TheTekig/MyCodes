print("Vamos calcular o tempo médio de sua viagem!!!")
#Entrada de Dados
distancia = float(input("Distancia que irá percorrer(km):"))
velocidade= float(input("Velocidade esperada (km/h):"))
#Calculo 
tempo = distancia / velocidade
float(tempo)
#Resultado
print("Tempo médio de sua viagem é de %.2f horas" %(tempo))