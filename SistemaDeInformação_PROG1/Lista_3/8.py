paisA = float(input("Habitantes Iniciais Pais A ---> "))
paisB = float(input("Habitantes Iniciais Pais B ---> "))
Agrow = float(input("Porcentagem de crescimento Iniciais Pais A ---> %"))
Bgrow = float(input("Porcentagem de crescimento Iniciais Pais B ---> %"))
Agrow = Agrow / 100
Bgrow = Bgrow / 100
year = 0

if paisA <= paisB:
    while paisA <= paisB:
        paisA = (paisA * Agrow) + paisA
        paisB = (paisB * Bgrow) + paisB
        year = year + 1
else:
    while paisB <= paisA:
        paisA = (paisA * Agrow) + paisA
        paisB = (paisB * Bgrow) + paisB
        year = year + 1




print(f"Pais A ---> {paisA}\nPais B ---> {paisB}\nAnos Para Superar ---> {year}")