# Problema H - Haja Ordenação
###### [Caminho para Codeforces](https://codeforces.com/gym/103388/problem/H)
O contexto deste exercício se trata de um problema onde nos perguntamos se podemos ordenar uma lista de blocos com cores e valores ou não. Cada bloco pertence a um grupo de cor e possui um valor numérico único, e só podemos trocar blocos de lugar que pertencem à mesma cor.

A minha solução foi feita utilizando a seguinte lógica:

Como cada bloco na lista possui um valor numérico crescente único, exemplo: $1,2,3,4,5,6,7,8,...$, nós podemos verificar se é possível ordená-la ao simplesmente fazermos um loop de 0 a $N-1$, onde $N$ é a quantidade de blocos.

Teremos duas arrays/vetores um vetor de `set<int>` para armazenar todos os numeros em suas respectivas cores, `valorPorCor[cor].insert(valor);` e um vetor de `int` que guardará a sequencia das cores que foram lidas, pois essa sequencia importa.

A ideia básicamente então consiste em ir iterando cada bloco no array de `valorPorCor` e ir verificando se existe um bloco na mesma cor que o bloco atual com valor equivalente à posição atual + 1. 

- Se não houver, já podemos parar o loop e imprimir "N", indicando que não existe como ordenarmos os blocos. 
- Se o loop terminar normalmente, significa que podemos ordenar a lista e poderemos imprimir "Y". 

Exemplo:

```
# valor_por_cor: guarda todos os valores recebidos em um set para fazer a busca mais rapidamente. (o set pode acabar ordenando esses valores, por esse motivo iremos buscar os valores de acordo com a sequencia de cores)
# sequencia_de_cores: guardara do indice 0 ao quantidadeBlocos-1 toda a sequencia das cores.

para bloco=0 enquanto bloco<quantidadeBlocos então faça:
    cor = sequencia_de_cores[bloco];
    se (valor_por_cor[cor].naoEncontrou(bloco+1)): # como o primeiro valor da sequencia crescente é 1 e não zero, devemos primeiro buscar por "+1"
        mostrar "N\n";
        finalizar;    
    bloco+=1;
```

A verificação de que se existe um bloco em uma cor pode ser feita de maneira mais rápida se usarmos a estrutura set durante o input dos blocos para registrarmos que valores existem em cada cor, por isso a sugestão anteriormente do uso de set.

O exercicio deseja que a gente consiga mostrar 1 2 3 4 5 6 ... em ordem, mas para isso podemos trocar os blocos se forem da mesma cor, porém estiverem em ordem inversas, por exemplo:

Esse exemplo abaixo não é possivel, pois não existe numero 1 na cor 2 para trocar e colocar no começo.

```
<numero, cor>
<3,2>
<1,1>
<2,3>
```

Veja as iterações com a lógica:

- valor_por_cor: [[],[1],[3],[2]]
- sequencia_de_cores: [2,1,3]

Logo na primeira iteração, ou seja, na iteração $0$ o código vai tentar buscar pela sequencia_de_cores[0], no caso o $2$, e quando for acessar o valor_por_cor[2] ele terá em sua disposição o numero $3$ apenas, pois só esse foi guardado no grupo de cores $2$. Como ele está na primeira iteração ($0$), então ele está procurando pelo valor $0+1$.

O código de busca seria: `valor_por_cor[cor].naoEncontrou(bloco+1)`, ou seja, `valor_por_cor[2].naoEncontrou(1) ?`, a resposta para esse cara seria $true$, pois o valor 1 não existe no grupo de valor da cor 2, como observado anteriormente,

Como pode observar, a gente precisa entender a ordem em que as cores e valores entraram, pois pode acontecer de fazer a verificação incorretamente, e dizer que o exemplo acima é possivel ordenar, sendo que não é, pois o <1,1> não pode subir para posição de <3,2> já que são cores difrentes.

Agora esse outro exemplo já é possivel, pois podemos trocar os valores <3,2> por <1,2> e os blocos irão ficar em ordem os valores.

```
<numero,cor>
<3,2>
<2,1>
<1,2>
<4,1>
<5,3>
<6,3>
```

#### Entendendo a lógica:

##### Exemplo de entrada 1:

[ _**3**_ ] [ 4 ] [ _**1**_ ] [ 2 ]

No exemplo acima, temos duas cores e quatro blocos e podemos prosseguir assim

- Index 0: verificamos se existe número 1 na mesma cor para botarmos no lugar, e vimos que existe, então continuamos;
- Index 1: verificamos se existe número 2 na mesma cor para botarmos no lugar, e prosseguimos;
- Index 2: verificamos se existe número 3 na mesma cor para botarmos no lugar, e prosseguimos;
- Index 3: verificamos se existe número 4 na mesma cor para botarmos no lugar, e vimos que existe, então finalizando o loop normalmente e indicando que podemos ordenar a lista;

##### Exemplo de entrada 2:

[ _**2**_ ] [ 4 ] [ _**1**_ ] [ 3 ]

No exemplo acima, também temos duas cores e quatro blocos e podemos prosseguir assim

- Index 0: verificamos se existe número 1 na mesma cor para botarmos no lugar, e vimos que existe, então continuamos;
- Index 1: verificamos se existe número 2 na mesma cor para botarmos no lugar, e percebemos que não existe, assim quebrando o loop e imprimindo "N", indicando que não podemos ordenar a lista;


Material Complemetnar:
- [Vector of sets in C++](https://www.geeksforgeeks.org/vector-of-sets-in-c/)

