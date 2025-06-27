#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

int main()
{
    SetConsoleOutputCP(CP_UTF8);

    char player1[256];
    char player2[256];
    printf("=== Pedra === Papel === Tesoura ===\n");
    printf("\nPlayer 1 ---> ");
    scanf("%s",&player1);
    printf("Player 2 ---> ");
    scanf("%s",&player2);

    printf("%s --- %s",player1,player2);

    if (strcmp(player1 , "papel") == 0 )
    {

        if(strcmp(player2 , "papel") == 0)
        {
            printf("\nEmpate!");
        }
        else if (strcmp(player2, "tesoura") == 0)
        {
            printf("\nPlayer 2 Ganhou!");
        }
        else if (strcmp(player2, "pedra") == 0 )
        {
            printf("\nPlayer 1 Ganhouh!");    
        }
        else
        {
            printf("\nValor digitado pelo Player 2 Invalido!");
        }
        
    }
     else if (strcmp(player1 , "tesoura") == 0 )
    {

        if(strcmp(player2 , "papel") == 0)
        {
            printf("\nPlayer 1 Ganhouh!");
        }
        else if (strcmp(player2, "tesoura") == 0)
        {
            printf("\nEmpate!");
        }
        else if (strcmp(player2, "pedra") == 0 )
        {
            printf("\nPlayer 2 Ganhouh!");    
        }
        else
        {
            printf("\nValor digitado pelo Player 2 Invalido!");
        }
        
    }
      else if (strcmp(player1 , "pedra") == 0 )
    {

        if(strcmp(player2 , "papel") == 0)
        {
            printf("\nPlayer 2 Ganhouh!");
        }
        else if (strcmp(player2, "tesoura") == 0)
        {
            printf("\nPlayer 1 Ganhou!");
        }
        else if (strcmp(player2, "pedra") == 0 )
        {
            printf("\nEmpate!");    
        }
        else
        {
            printf("\nValor digitado pelo Player 2 Invalido!");
        }
        
    }
    else
    {
        printf("\nValor digitado pelo Player 1 Invalido!");
    }
    



    return 0;
}