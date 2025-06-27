#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

void main()
{
    //Habilitando Acentuação
    SetConsoleOutputCP(CP_UTF8);    

    //Declarando Variaveis
    int hora_cinema , hora_atual , hora_atrasada; 
    
    //Entrada de Dados
    printf("\nDigite o horário do cinema:");
    scanf("%d" , &hora_cinema);
    printf("\nDigite a hora atual:");
    scanf("%d" , &hora_atual);

    hora_atrasada = hora_cinema + 30;

    //Condicionais
    if (hora_cinema < hora_atual)
    {

        printf("\nO filme ainda não começou!");

    }
    else if (hora_cinema > hora_atrasada)
    {

        printf("\nVocê esta atrasado, o filme já acabou!");

    }
    else
    {

        printf("\nVocê esta no horário, pode entrar para ver o filme!");

    }

    return 0;
}