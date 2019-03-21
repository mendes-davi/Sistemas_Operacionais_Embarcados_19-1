1. Crie um código em C que escreve a sequência de Fibonacci em arquivo em formato binário. Comece a sequência com os valores 0 e 1, e grave suas primeiras 100 posições em arquivo.

```c
#include <stdio.h>
#include <stdlib.h>

long int fib(int n);

int main(int argc, char const *argv[])
{
	FILE * fp;
	if(!(fp = fopen("fib.bin","wb")))
	{
		printf("Erro ao abrir o arquivo\n");
		return 0;
	}
	for (int i = 0; i <= 100; ++i)
	{
		long int data = fib(i);
		fwrite(&data,sizeof(long int),1,fp);
	}
	fclose(fp);
	return 0;
}


long int fib(int n) //Fib optimised to Time Complexity: O(n)
{ 
  long int a = 0, b = 1, c, i; 
  if( n == 0) 
    return a; 
  for (i = 2; i <= n; i++) 
  { 
     c = a + b; 
     a = b; 
     b = c; 
  } 
  return b; 
}
```

2. Crie um código em C que lê o arquivo da questão anterior e escreve os valores lidos da sequência de Fibonacci na tela.

```c
#include <stdio.h>
#include <stdlib.h>

long int fib(int n);

int main(int argc, char const *argv[])
{
	FILE * fp;
	long int read;
	if(!(fp = fopen("fib.bin","rb")))
	{
		printf("Erro ao abrir o arquivo\n");
		return 0;
	}
	while(!feof(fp))
	{
		fread(&read,sizeof(long int),1,fp);
		printf("%ld\t", read);
	}
	fclose(fp);
	return 0;
}
```


