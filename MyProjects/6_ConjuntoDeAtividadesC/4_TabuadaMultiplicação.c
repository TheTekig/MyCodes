#include <stdio.h>
#include <stdlib.h>

int main(){
    
int num,cont,res,max;
    
printf("Vamos fazer a tabuada!\nDigite o numero que deseja saber a tabuada:");    
scanf("%d", &num);
    
printf("\nDigite o numero maximo da tabuada:");
scanf("%d", &max);
    
printf("\n\tTabuada do %d\n\n", num);   
cont = 0;
if (num < 0)
{
    printf("Numero invalido!\n");
}
else
{
    while (cont <= max)
        {
            res = num * cont;
            printf("%d x %d = %d\n", num, cont, res);
            cont = cont + 1;
        }
    
        
    printf("\n\tFim da tabuada!\n");
}
    return 0;
}
