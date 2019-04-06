1. Apresente as características e utilidades das seguintes funções:

(a) `popen()`

> A função abre um processo através da criação de um pipe, forking e invoca o shell. `FILE *popen(const char *command, const char *type);` e `type` indica o sentido do pipe (leitura ou escrita).

(b) `pclose()`

> A função fecha o `stream` aberto por `popen()` e apresenta o seguinte protótipo `int pclose(FILE *stream);`.

(c) `fileno()`

> A função retorna o descritor de arquivo do tipo inteiro associado com a `stream` apontada. `int fileno(FILE *stream); `

2. Quais são as vantagens e desvantagens em utilizar:

(a) `popen()?`

> `popen()` é usado quando se deseja um ponteiro e tem funcionamento similar ao de um arquivo.

(b) `exec()?`

> `exec()` permite escutar um comando e substituir o conteúdo de um processo.