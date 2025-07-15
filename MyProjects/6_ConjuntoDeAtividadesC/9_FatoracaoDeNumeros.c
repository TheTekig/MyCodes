#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

int fatoracao(int num)
{
    int i,g;
    printf("Fatoracao de %d: ",num);
    g = 1;
    for(i = 1;i < num;i++)
    {     
        g *= i + 1;
       printf("\n%d",g);
    }
}


int main()
{
int num;
printf("Enter a number: ");
scanf("\n%d",&num);
fatoracao(num);
