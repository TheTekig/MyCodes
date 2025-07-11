#include <stdio.h>
#include <stdlib.h>



void imprimeIntervaloDecrescente(int valinicial, int valfinal, int opcao)
{
        while (valinicial >= valfinal)
            {
                if (opcao == 1)
                {
                    if (valinicial % 2 == 0)
                    {
                        printf("%d\n", valinicial);
                    }
                }
                else if (opcao == 2)
                {
                    if (valinicial % 2 != 0)
                    {
                        printf("%d\n", valinicial);
                    }
                }
                else
                {
                    printf("%d\n", valinicial);
                }
                
                valinicial--;
            }
}

void imprimeIntervaloCrescente(int valinicial, int valfinal, int opcao)
{

        while (valinicial <= valfinal)
            {    
                if (opcao == 1)
                {
                    if (valinicial % 2 == 0)
                    {
                        printf("%d\n", valinicial);
                    }
                }
                else if (opcao == 2)
                {
                    if (valinicial % 2 != 0)
                    {
                        printf("%d\n", valinicial);
                    }
                }
                else
                {
                    printf("%d\n", valinicial);
                }
                
                valinicial++;
            }
}

int opcoes()
{
    int opcao;
    printf("\n\tDeseja Imprimir:\n");
    printf("\n1 - Sómente os pares");
    printf("\n2 - Somente os impares");
    printf("\n3 - Todos os numeros");
    printf("\n\n\tOpcao: ");
    scanf("%d", &opcao);
    
    while (opcao < 1 || opcao > 3)
        {
            printf("Opcao invalida, digite novamente: ");
            scanf("%d", &opcao);
        }
    return opcao;
}


int main(){
    
int valinicial, valfinal, opcao;
    
    printf("\n\t-=-Programa que imprime os numeros de um intervalo-=-\n");
    
    printf("\nDigite o valor inicial: ");
    scanf("%d", &valinicial);
    
    printf("Digite o valor final: ");
    scanf("%d", &valfinal);
    
    opcao = opcoes();
  
    if (valinicial == valfinal)
    {
        printf("\nOs valores sao iguais!\n");
    }
    else if (valinicial < valfinal)
    {
        printf("\nOrdem crescente:\n\n");
        imprimeIntervaloCrescente(valinicial, valfinal,opcao);
    }
    else 
    {
        printf("Ordem decrescente:\n");
        imprimeIntervaloDecrescente(valinicial, valfinal,opcao);
    }
    printf("\nFim da Lista\n");
        

        
    return 0;
}
