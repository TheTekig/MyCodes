#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

void main()
{
    SetConsoleOutputCP(CP_UTF8);   
    char name[256];
    char last_name[256];
    int age;
    int birthday;

    printf("Name --->");
    scanf("%s" , &name);
    printf("Lastname --->");
    scanf("%s" , &last_name);
    printf("Age --->");
    scanf("%d" , &age);
    printf("Birthday --->");
    scanf("%d" , &birthday);

    printf("Olá %s %s!\nVocê nasceu em %d e possui %d anos! " , name,last_name,birthday,age);

    return 0;    
}