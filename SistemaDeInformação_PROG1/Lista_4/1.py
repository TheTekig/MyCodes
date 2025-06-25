

num = int(input("Número ---> "))
cont = 1

while num > 0:
   
  cont *= num 
  
  num = num - 1  
   
print(f"numero --> {num}\nfator --> {cont}")