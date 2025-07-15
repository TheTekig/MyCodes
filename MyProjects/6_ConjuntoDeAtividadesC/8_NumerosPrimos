#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

int numerosPrimos(int num)
{
    int i,cont = 0;
    
    for(i = 1; i <= num; i++)
        {
            if (num % i == 0)
            {
                printf("%d\n", i);
                cont++;
                if (i == 1 || i == num)
                {
                    if (cont == 2)
                    {
                        return 1;
                    }
                }
            
            }
        }
        return 0;
}


int main()
{
int num;
printf("Numeros Primos: ");
scanf("%d", &num);
    printf("\nOs divisores de %d sao:\n", num);
if  (numerosPrimos(num) == 1)
{
    printf("\n%d eh um numero primo!\n" , num);
}
else
{
    printf("\n%d nao eh um numero primo!\n" , num);
}


}
