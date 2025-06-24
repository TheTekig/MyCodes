num1 = float(input("Primeiro Número ---> "))
num2= float(input("Segundo Número ---> "))
num3 = float(input("Terceiro Número ---> "))

pos1 = None
pos2 = None
pos3 = None

if num1 > num2 and num1 > num3:

    if num2 > num3:
        pos1 = num1
        pos2 = num2
        pos3 = num3
    else:
        pos1 = num1
        pos2 = num3
        pos3 = num2
elif num2 > num3 and num2 > num1:
    
    if num3 > num1:
        pos1 = num2
        pos2 = num3
        pos3 = num1
    else:
        pos1 = num2
        pos2 = num1
        pos3 = num3
else:
     
     if num1 > num2:
        pos1 = num3
        pos2 = num1
        pos3 = num2
     else:
        pos1 = num3
        pos2 = num2
        pos3 = num1

print("Maior Número ---> %.2f\tMenor Número ---> %.2f\nOrdem Decrescente ---> %.2f - %.2f - %.2f " %(pos1,pos3,pos1,pos2,pos3))
         
    