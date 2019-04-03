1. Como se utiliza o comando `ps` para:

(a) Mostrar todos os processos rodando na máquina?
`ps -e`
(b) Mostrar os processos de um usuário?
`ps -u [user name]`
(c) Ordenar todos os processos de acordo com o uso da CPU?
`ps --sort=-pcpu`
(d) Mostrar a quanto tempo cada processo está rodando?
`ps -e -o etime`
2. De onde vem o nome `fork()`?

> Fork (bifurcação) permite criar uma cópia exata do processo que chama a função.

3. Quais são as vantagens e desvantagens em utilizar:

(a) `system()`?

> Permite executar um comando dentro de um programa, criando um subprocesso. Ela retorna em sua saída o status do comando no shell. Se o shell não puder ser executado,o system() retorna o valor 127 e se outro erro ocorrer, retorna o valor -1. O uso do system não é recomendado para todos os casos, pois mesmo sendo simples, dá brechas à falhas de execução pois depende muito do sistema.

(b) `fork()` e `exec()`?

> Não existe uma função que crie e execute um novo processo em um único passo. Para isso, utiliza-se a função fork() para criar uma cópia exata do processo e então, com a função exec(), substitui o conteúdo desse processo criado, criando um novo processo.


4. É possível utilizar o `exec()` sem executar o `fork()` antes?

> Sim, porém o conteúdo do processo será totalmente alterado. 

5. Quais são as características básicas das seguintes funções:
(a) `execp()`?
> Permite que o nome ou a procura do programa esteja no caminho atual, ou "current path".

(b) `execv()`?
> Permite que a lista de argumentos do novo programa seja nula mas requer o caminho completo para execução do comando.

(c) `exece()`?
> Permite que haja um argumento adicional no novo programa.

(d) `execvp()`?
> Permite que o nome ou a procura do programa esteja no caminho atual e que a lista de argumentos do novo programa seja nula.

(e) `execve()`?
> Permite que o nome ou a procura do programa esteja no caminho atual e que haja um argumento adicional no novo programa .

(f) `execle()`?
>Permite que os mecanismos de var args sejam utilizados e que haja um argumento adicional no novo programa.


