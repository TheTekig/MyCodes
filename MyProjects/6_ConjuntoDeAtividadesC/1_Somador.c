#include <stdio.h>
#include <stdlib.h>

int entradaDados(void){

    int num, num2;

  printf("Digite um numero: ");
  scanf("%d", &num);
  printf("Digite outro numero: ");
  scanf("%d", &num2);

  return num + num2;
}


int main(void) {

  int soma = entradaDados();
  printf("A soma dos numeros e: %d", soma);
  
}
