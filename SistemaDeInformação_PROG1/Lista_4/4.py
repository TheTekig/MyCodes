num = int(input("Numero ---> ")) 
primeiro = 1
segundo = 1

while num != 0:

   ordem = primeiro + segundo
   primeiro = segundo
   segundo = ordem

   num = num-1

   print (primeiro,segundo,ordem)