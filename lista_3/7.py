paisA = 80000
paisB = 200000
Agrow = 0.03
Bgrow = 0.015
year = 0
while paisA <= paisB:
    paisA = (paisA * Agrow) + paisA
    paisB = (paisB * Bgrow) + paisB
    year = year + 1


print(f"Pais A ---> {paisA}\nPais B ---> {paisB}\nAnos Para Superar ---> {year}")