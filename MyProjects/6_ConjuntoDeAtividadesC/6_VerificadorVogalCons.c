#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

bool validarNome(char nome[100])
{
    int i;
    for(i = 0;i < strlen(nome);i++)
        {
            if (isalpha(nome[i]) == false)
            {
                return false;
            }
        }
    return true;
}

int main(){
    
    char nome[100];
    printf("\n\t-=-Programa para contar vogais e consoantes em um nome-=-\n");
    printf("\nDigite seu nome: ");
    scanf("%s", nome);
    while (validarNome(nome) == false)
        {
            printf("Digite um nome valido: ");
            scanf("%s", nome);
        }
    
    int i,Vcont,Ccont,LNome;

    Vcont = 0;
    Ccont = 0;
    LNome = strlen(nome);
    
    for(i = 0;i <= strlen(nome);i++) 
    {
        char letra = tolower(nome[i]);
        
        if (letra == 'a' || letra == 'e' || letra == 'i' || letra == 'o' || letra == 'u') 
        {
            Vcont++;
        }
        else if (isalpha(letra))
        {
            Ccont++;
        }
    }
    printf("\nSeu nome tem %d letras \n", LNome);
    printf("Quantidade de vogais: %d \n", Vcont);
    printf("Quantidade de consoantes: %d \n", Ccont);
        
    return 0;
}
