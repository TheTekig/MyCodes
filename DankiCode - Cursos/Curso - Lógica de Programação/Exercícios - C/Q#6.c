#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

void main()
{
    SetConsoleOutputCP(CP_UTF8);

    int idade;
    char nome[256];

    printf("Qual o seu nome?? --->");
    scanf("%s" , &nome);

    printf("Qual a sua idade --->");
    scanf("%d" , &idade);

    printf("\nNome ---> %s\t\tIdade ---> %d" , nome,idade);
    printf("\nA primeira letra do seu nome é ---> %c\n"  , nome[0] );
    
    if (idade < 12)
    {
        printf("Você é uma criança!");
    }
    else if (idade < 18)
    {
        printf("Você é um adolescente!");
    }
    else
    {
        printf("Você é um adulto!");
    }
    


    return 0;
}