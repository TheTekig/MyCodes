#include <stdio.h>
#include <stdlib.h>

int main(){
    
int valinicial, valfinal;
    
    printf("\n\t-=-Programa que imprime os numeros de um intervalo-=-\n");
    
    printf("\nDigite o valor inicial: ");
    scanf("%d", &valinicial);
    
    printf("Digite o valor final: ");
    scanf("%d", &valfinal);

    if (valinicial == valfinal)
    {
        printf("\nOs valores sao iguais!\n");
    }
    
    else if (valinicial < valfinal)
    {
        printf("\nOrdem crescente:\n\n");
    while (valinicial <= valfinal)
        {
            printf("%d\n", valinicial);
            valinicial++;
        }
    }
    else 
    {
        printf("Ordem decrescente:\n");
        while (valinicial >= valfinal)
            {
            printf("%d\n", valinicial);
            valinicial--;
            }
    }
    printf("\nFim da Lista\n");
    
    return 0;
}
