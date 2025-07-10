#include <stdio.h>
#include <stdlib.h>

int menu(){
    int opcao;
    printf("\n\tCalculadora\n\n");
    printf("\t1 - Soma\n");
    printf("\t2 - Subtracao\n");
    printf("\t3 - Multiplicacao\n");
    printf("\t4 - Divisao\n");
    printf("\t5 - Media\n");
    printf("\t6 - Sair\n");
    printf("\nEscolha uma opcao:");
    scanf("%d", &opcao);
    while (opcao < 1 || opcao > 6)
    {
        printf("\tOpcao invalida!\n");
        printf("Escolha uma opcao:\n");
        scanf("\n%d", &opcao);
    }
    return opcao;
}

void soma(a, b){
    int soma = a + b;
    printf("Resultado: %d\n", soma);

}

void subtracao(a, b){
    int subtracao = a - b;
    printf("Resultado: %d\n", subtracao);
    
}

void multiplicacao(a, b){
    int multiplicacao = a * b;
    printf("Resultado: %d\n", multiplicacao);
}

void divisao(a, b){
    int divisao = a / b;
    printf("Resultado: %d\n", divisao);
}

void media(a,b){
    int media;
    media = (a + b) / 2;
    printf("Resultado: %d\n", media);
}


int main(){
    int opcao, num1, num2;
    opcao = menu();
    
    while (opcao != 6){
        
        if (opcao == 1){
            printf("\n\tSoma\n");
            printf("Primeiro numero:");
            scanf("%d", &num1);
            printf("Segundo numero:");
            scanf("%d", &num2);
            soma(num1, num2);
            opcao = menu();
        }

        if (opcao == 2){
            printf("\n\tSubtracao\n");
            printf("Primeiro numero:");
            scanf("%d", &num1);
            printf("Segundo numero:");
            scanf("%d", &num2);
            subtracao(num1, num2);
            opcao = menu();
        }

        if (opcao == 3){
            printf("\n\tMultiplicacao\n");
            printf("Primeiro numero:");
            scanf("%d", &num1);
            printf("Segundo numero:");
            scanf("%d", &num2);
            multiplicacao(num1, num2);
            opcao = menu();
        }

        if (opcao == 4){
            printf("\n\tDivisao\n");
            printf("Primeiro numero:");
            scanf("%d", &num1);
            printf("Segundo numero:");
            scanf("%d", &num2);
            divisao(num1, num2);
            opcao = menu();
        }  
        
        if (opcao == 5){
            printf("\n\tMedia\n");
            printf("Primeiro numero:");
            scanf("%d", &num1);
            printf("Segundo numero:");
            scanf("%d", &num2);
            media(num1, num2);
            opcao = menu();
        }
    }
    
    printf("Saindo...\n");
    
    return 0;
}
