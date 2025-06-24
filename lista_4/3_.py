num1 = int (input("Número 1 --->"))
num2 = int (input("Número 2 --->"))

if num1 > num2:
    divisao = num1 / num2
    resto = num1%num2
    num1 = num2
    num2 = resto
else:
    divisao = num2 / num1
    resto = num2%num1
    num2 = num1
    num1 = resto

while resto != 0:
        
    if num1 > num2:
        divisao = num1 / num2
        resto = num1%num2
        num1 = num2
        num2 = resto
    else:
        divisao = num2 / num1
        resto = num2%num1
        num2 = num1
        num1 = resto

if num1 > num2:
    print("MMC ---> %d" %num1)

else:
    print("MMC ---> %d"%num2)




