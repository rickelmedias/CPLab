# Problema H - Haja Ordenação
###### [Caminho para Codeforces](https://codeforces.com/gym/103388/problem/H)
O contexto deste exercício se trata de um problema onde nos perguntamos se podemos ordenar uma lista de blocos com cores e valores ou não. Cada bloco pertence a um grupo de cor e possui um valor numérico único, e só podemos trocar blocos de lugar que pertencem à mesma cor.

A minha solução foi feita utilizando a seguinte lógica:
Como cada bloco na lista possui um valor numérico crescente único, nós podemos verificar se é possível ordená-la ao simplesmente fazermos um loop de 0 a N(quantidade de blocos) - 1, iterando cada bloco na lista e verificando se existe um bloco na mesma cor que o bloco atual com valor equivalente à posição atual + 1. Se não houver, já podemos parar o loop e imprimir "N", indicando que não existe como ordenarmos os blocos. Se o loop terminar normalmente, significa que podemos ordenar a lista e poderemos imprimir "Y". 

A verificação de que se existe um bloco em uma cor pode ser feita de maneira mais rápidas se usarmos a estrutura set durante o input dos blocos para registrarmos que valores existem em cada cor.


#### Exemplo de entrada 1:

[ **3** ] [ 4 ] [ **1** ] [ 2 ]

No exemplo acima, temos duas cores e quatro blocos e podemos prosseguir assim

- Index 0: verificamos se existe número 1 na mesma cor para botarmos no lugar, e vimos que existe, então continuamos;
- Index 1: verificamos se existe número 2 na mesma cor para botarmos no lugar, e prosseguimos;
- Index 2: verificamos se existe número 3 na mesma cor para botarmos no lugar, e prosseguimos;
- Index 3: verificamos se existe número 4 na mesma cor para botarmos no lugar, e vimos que existe, então finalizando o loop normalmente e indicando que podemos ordenar a lista;

#### Exemplo de entrada 2:

[ **2** ] [ 4 ] [ **1** ] [ 3 ]

No exemplo acima, também temos duas cores e quatro blocos e podemos prosseguir assim

- Index 0: verificamos se existe número 1 na mesma cor para botarmos no lugar, e vimos que existe, então continuamos;
- Index 1: verificamos se existe número 2 na mesma cor para botarmos no lugar, e percebemos que não existe, assim quebrando o loop e imprimindo "N", indicando que não podemos ordenar a lista;
