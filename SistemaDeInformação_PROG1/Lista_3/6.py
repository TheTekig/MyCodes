x = 1
par = 0
impar = 0
maiornum = 0
num = 0
mnum = 0

while True:

    num = int(input("Digite um número -->"))

    if num == -1:
        break
        
    while num < 1 or num > 1000:
        num = int(input("Numero Invalido! Digite Novamente -->"))

    if (num % 2) == 0:
        par = par + 1

    else:
        impar = impar + 1
    
    mnum = num
    if mnum >= num:
        if maiornum < mnum:
            maiornum = mnum

print(f"par --> {par}\nimpar --> {impar}\nmaior --> {maiornum}")

