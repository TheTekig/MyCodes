#include <stdio.h>
#include <stdlib.h>

int main(){
    
int num,cont = 0,res;
printf("Vamos fazer a tabuada!\nDigite o numero que deseja saber a tabuada:");    
scanf("%d", &num);
printf("\n\tTabuada do %d\n\n", num);
while (cont <= 10)
    {
        res = num * cont;
        printf("%d x %d = %d\n", num, cont, res);
        cont = cont + 1;
    }

    
printf("\n\tFim da tabuada!\n");
    return 0;
}
