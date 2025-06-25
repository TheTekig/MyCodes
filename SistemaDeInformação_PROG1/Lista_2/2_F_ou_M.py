print("\nVerificação de gênero, digite 'm' para masculino ou 'f' para feminino!\n")
def entrada_de_dados():

    genero  = str(input("Digite a letra: "))
  
    validacao(genero)

def validacao(genero):
    masculino = "m" 
    feminino  = "f" 
    if (genero == masculino):
        print("Gênero masculino foi selecionado")
    elif(genero == feminino):
        print("Gênero feminino foi selecionado")
    else:
        print("Sexo Inválido")

entrada_de_dados()