1. Crie um programa em C que preenche matrizes `long int A[60][60]` e `long int B[60][60]` completamente com valores aleatórios (use a função `random()`), e que calcula a soma das duas matrizes por dois métodos:

(a) De forma sequencial;

```c
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

#include <sys/types.h>
#include <sys/stat.h>

#define N 60

int main(int argc, char const *argv[])
{
	long int A[N][N], B[N][N];
	long long int SUM[N][N];
	for (int i = 0; i < N; ++i) //Populando matrizes
	{
		for (int j = 0; j < N; ++j)
		{
			A[i][j] = random();
			B[j][i] = random(); // i,j ou j,i - nao importa!
		}
	}

	for (int i = 0; i < N; ++i) //Somando sequencialmente
	{
		for (int j = 0; j < N; ++j)
		{
			SUM[i][j] = A[i][j]+B[i][j];
		}
	}
	return 0;
}
```

(b) De forma paralela.

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

#include <sys/types.h>
#include <sys/stat.h>

#define N 60

#define SLICES 4

long int A[N][N], B[N][N];
long long int SUM[N][N], SUM_T[N][N];

void* soma_arrays(void* params)
{
	int i, j; 
	int slice = (int)params; 

	for (i = slice * N / 4; i < (slice + 1) * N / 4; i++)
	{ 
		for (j = 0; j < N; j++)
		{ 
			SUM_T[i][j] = A[i][j] + B[i][j]; 
		} 

	}
	return NULL;
}

int main(int argc, char const *argv[])
{
	pthread_t pthr[SLICES];
	int step = 0;
	for (int i = 0; i < N; ++i) //Populando matrizes
	{
		for (int j = 0; j < N; ++j)
		{
			A[i][j] = random();
			B[j][i] = random(); // i,j ou j,i - nao importa!
		}
	}

	//PARALELO
	for (int i = 0; i < SLICES; i++) { 
		pthread_create(&pthr[i], NULL, &soma_arrays, (void*) step); 
		step++; 
	} 
	for (int i = 0; i < SLICES; i++) { 
		pthread_join(pthr[i], NULL); 
	}

	//Validando
	for (int i = 0; i < N; ++i)
	{
		for (int j = 0; j < N; ++j)
		{
			if (SUM[i][j] != SUM_T[i][j])
				equal = 0;
		}
	}
	equal == 1 ? printf("DEU BOM\n") : printf("DEU RUIM\n"); 

	return 0;
}
```

Ao final do programa principal, compare os resultados obtidos pelos dois métodos.

> Os resultados obtidos foram iguais!

2. Repita o exercício anterior, mas calcule o produto matricial `A*B`.

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

#include <sys/types.h>
#include <sys/stat.h>

#define N 60

#define SLICES 4

long int A[N][N], B[N][N];
long long int C[N][N], C_T[N][N];
int step_i = 0; 

void* mult_arrays(void* params)
{
	int core = step_i++; 
	for (int i = core * N / 4; i < (core + 1) * N / 4; i++) 
		for (int j = 0; j < N; j++) 
			for (int k = 0; k < N; k++) 
				C_T[i][j] += A[i][k] * B[k][j]; 
	return NULL;
}

int main(int argc, char const *argv[])
{
	pthread_t pthr[SLICES];
	int equal = 1;
	for (int i = 0; i < N; ++i) //Populando matrizes
	{
		for (int j = 0; j < N; ++j)
		{
			A[i][j] = random();
			B[j][i] = random(); // i,j ou j,i - nao importa!
		}
	}

	// SEQUENCIAL
	for (int i = 0; i < N; i++) 
		for (int j = 0; j < N; j++) 
			for (int k = 0; k < N; k++) 
				C[i][j] += A[i][k] * B[k][j]; 

	//PARALELO
	for (int i = 0; i < SLICES; i++) 
		pthread_create(&pthr[i], NULL, &mult_arrays, NULL); 
	for (int i = 0; i < SLICES; i++) 
		pthread_join(pthr[i], NULL);

	//Validando
	for (int i = 0; i < N; ++i)
	{
		for (int j = 0; j < N; ++j)
		{
			if (C[i][j] != C_T[i][j])
				equal = 0;
		}
	}
	equal == 1 ? printf("DEU BOM\n") : printf("DEU RUIM\n");	 



	return 0;
}
```

3. Repita o exercício anterior, mas calcule o produto da matriz `long int A[60][60]` por um escalar `long int x`

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

#include <sys/types.h>
#include <sys/stat.h>

#define N 60

#define SLICES 4

long int A[N][N];
long long int C[N][N], C_T[N][N];
long int x = 2; // Escalar para multiplicar

void* escalar_arrays(void* params)
{
	int i, j; 
	int slice = (int)params; 

	for (i = slice * N / 4; i < (slice + 1) * N / 4; i++)
	{ 
		for (j = 0; j < N; j++)
		{ 
			C_T[i][j] = A[i][j] * x;
		} 

	}
	return NULL;
}

int main(int argc, char const *argv[])
{
	pthread_t pthr[SLICES];
	int step = 0;
	int equal = 1;
	for (int i = 0; i < N; ++i) //Populando matrizes
	{
		for (int j = 0; j < N; ++j)
		{
			A[i][j] = random();
		}
	}

	//Sequencial
	for (int i = 0; i < N; ++i)
	{
		for (int j = 0; j < N; ++j)
		{
			C[i][j] = A[i][j] * x;
		}
	}

	//PARALELO
	for (int i = 0; i < SLICES; i++) { 
		pthread_create(&pthr[i], NULL, &escalar_arrays, (void*) step); 
		step++; 
	} 
	for (int i = 0; i < SLICES; i++) { 
		pthread_join(pthr[i], NULL); 
	}

	//Validando
	for (int i = 0; i < N; ++i)
	{
		for (int j = 0; j < N; ++j)
		{
			if (C[i][j] != C_T[i][j])
				equal = 0;
		}
	}
	equal == 1 ? printf("DEU BOM\n") : printf("DEU RUIM\n"); 

	return 0;
}
```