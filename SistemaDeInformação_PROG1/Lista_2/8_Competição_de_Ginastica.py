
candidatos = []
juiz = []
media = []

def inserir_candidatos():

    candidatos.append(str(input("Nome da Candidata: ")))
 
def inserir_notas_juiz(): 


    juiz.append(int(input("Nota Primeiro Juiz ---> ")))
    juiz.append(int(input("Nota Segundo Juiz ---> ")))
    juiz.append(int(input("Nota Terceiro Juiz ---> ")))
    juiz.append(int(input("Nota Quarto Juiz ----> ")))
    juiz.append(int(input("Nota Quinto Juiz ---> ")))

    juiz.sort()
    nota_maior = juiz.pop(-1)
    nota_menor = juiz.pop(0)
    media.append(sum(juiz) / len(juiz))
    print("A maior nota foi ---> %d\nA menor nota foi --->%d"%(nota_menor,nota_maior))
    #print(juiz)
    #print(media)
    #print(candidatos)
    
    juiz.clear()
    return(nota_maior,nota_menor)
def comparacoes():
    inserir_candidatos()
    inserir_notas_juiz()
    print(candidatos[-1])
    print("média ---> %.2f" %(media[-1]))
   

def iniciar():
    x=0
    while x<=2:
        comparacoes()
    x+=1
    

iniciar()   
print(media)

