#include <stdio.h>
#include <stdlib.h>


void main()
{
   int limite = 10;
   int contador = 1 ;

    while (contador <= limite) 
    { 
        
       if (contador == 5)
        {
            int contador2 = 10;

            while(contador2 > 0)
            {

               
                printf("BYE WORLD %d\n" , contador2);
                contador2--;

            }


        }

        printf("%d Hello World\n" , contador);
        contador++;
    }
    return 0;
}