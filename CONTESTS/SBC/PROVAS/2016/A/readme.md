# Problema A - Andando no Tempo
###### [Caminho para BeeCrowd](https://www.beecrowd.com.br/judge/pt/problems/view/2235)

Neste exercício, o usuário vai definir os valores para as fichas A,B e C.
Um detalhe a ser observado é que a ordem das fichas não determina o curso da viagem, pois o usuário pode viajar com a ficha A e retornar com a C, sem utilizar a B por exemplo, ou ir ao passado com a C e voltar com a B, existem várias combinações/possibilidades entre as fichas!
Outro detalhe a ser observado, é que o usuário pode somar as fichas para viajar para o futuro ou para o passado, podendo ou não escolher utilizar a ficha restante. Por exemplo: viajar ao futuro com as fichas A e B e retornar com a C, ou viajar ao passado com a B e C e ir ao futuro com a A.
Uma vez compreendido este conceito, basta programarmos as condições em que uma ficha anule a outra, pois significa que o usuário viajou para o passado/futuro e retornou ao presente, pois o a diferença entre os anos viajados seriam zero, lembrando que temos condições de viagem utilizando duas fichas ou utilizando as três. Importante ter em mente que o usuário só volta ao presente caso as diferenças de anos entre as fichas utilizadas se anulem!

##### ENTRADA 
A entrada consiste de uma linha contendo os valores dos três créditos $A$, $B$ e $C$ $(1 <= A, B, C <= 1000)$.

##### SAÍDA 
Seu programa deve imprimir uma linha contendo o caractere “S” se é possível viajar e voltar para o presente, ou “N” caso contrário.

Exemplo de Entrada   | Exemplo de Saída
-------------------- | ----------------
22 5 22              |       S
31 110 79            |       S
49 8 7               |       N

##### LÓGICA DA SOLUÇÃO


| Condição       | Expressão Matemática                                            | Saída     |
|----------------|-----------------------------------------------------------------|-----------|
| Condição 1     | $\((a - b = 0) \vee (a - c = 0) \vee (b - c = 0)\)$             | Mostrar S |
| Condição 2     | $\((a + b - c = 0) \vee (b - a + c = 0) \vee (c - a + b = 0)\)$ | Mostrar S |
| Condição 3     | $\((a - b - c = 0) \vee (b - a - c = 0) \vee (c - a - b = 0)\)$ | Mostrar S |
| Caso contrário | $\text{Caso nenhuma condição anterior seja verdade}$            | Mostrar N |

O símbolo matemático $\vee$, representa uma disjunção, operador ou (em inglês: OR), ou seja, em caso de acontecer $\((a - b = 0)$ ou $(a - c = 0)$ ou $(b - c = 0)\)$, o programa deverá mostrar a saída "S". Verifique aqui uma [lista de símbolos matemáticos](https://pt.wikipedia.org/wiki/Lista_de_símbolos_matemáticos) e seu significado, caso você esteja interessado em representar esses símbolos utilizando latex, [pode verificar esse conteúdo](https://oeis.org/wiki/List_of_LaTeX_mathematical_symbols).
