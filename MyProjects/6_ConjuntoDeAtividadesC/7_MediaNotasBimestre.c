#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>


int mediaNotas(int n1,int n2,int n3,int n4,int contador)
{
    int media;
    media = (n1+n2+n3+n4)/contador;
    printf("A media das notas e: %d",media);
}

int Notas(c , n)
{
    printf("Digite a %d nota: ",c);
    scanf("%d",&n);
    while(isdigit(n) != false)
        {
            printf("Somente Números \nDigite a %d nota: ",c);
            scanf("%d",&n);
        }
    return n;
}

int main()
{
    int nota1,nota2,nota3,nota4,media,contador;
    contador = 1;

    nota1 = Notas(contador,nota1);
    contador++;
    nota2 = Notas(contador,nota2);
    contador++;
    nota3 = Notas(contador,nota3);
    contador++;
    nota4 = Notas(contador,nota4);
  
    media = mediaNotas(nota1,nota2,nota3,nota4,contador);

    return 0;
}
