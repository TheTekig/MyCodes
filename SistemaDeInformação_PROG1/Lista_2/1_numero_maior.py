print("\nVamos ver qual número é maior!!!\n")

def entrada_de_dados():
    num1 = float(input("Coloque o primeiro número: "))
    num2 = float(input("Coloque o segundo número: "))
    calculos(num1,num2)
    
def calculos(num1,num2):

    if (num1 > num2):
        print("O número %0.1f é maior que o número %0.1f" %(num1 , num2))
    elif(num1 < num2):
        print("O número %0.1f é maior que o número %0.1f" %(num2 , num1)) 
    elif(num1 == num2):
        print("O número %0.1f é igual ao número %0.1f" %(num1 , num2))


entrada_de_dados()