# Problema F - Fase
###### [Caminho para Beecrowd](https://beecrowd.com.br/judge/pt/problems/view/2663)

Para resolver esse problema, primeiro recebemos como entrada o número de interações, o valor mínimo de vencedores desejado e todas as pontuações obtidas. Em seguida, utilizamos o algoritmo de ordenação Merge Sort para organizar as pontuações em ordem crescente.

Uma vez que as pontuações estão ordenadas, podemos encontrar o vencedor mínimo acessando o elemento no índice minVencedor - 1 do array ordenado. Em seguida, usamos um loop "for" para iterar pelas pontuações no array e somamos 1 ao contador enquanto a pontuação atual for menor ou igual à pontuação limite desejada. Quando encontramos uma pontuação maior que a pontuação limite, interrompemos o loop e imprimimos o contador, que representa o número de vencedores atingidos.

A complexidade assintótica desse algoritmo é O(n*log(n)), devido ao uso do Merge Sort para ordenar as pontuações. Isso significa que o desempenho do algoritmo cresce de forma logarítmica em relação ao tamanho da entrada, o que o torna eficiente para lidar com grandes conjuntos de dados.

Uma dica é usar a função de *sort()* que já vem por padrão nas bibliotecas e linguagens de programação, foi testado e funcionou bem para o exercício. Segue algumas referências:

- Como ordenar por ordem decrescente ou crescente:
  - [C++](https://www.geeksforgeeks.org/sort-c-stl/)
  - [Python](https://www.freecodecamp.org/news/python-sort-list-how-to-order-by-descending-or-ascending/)

<details>
  <summary>Clique aqui para ver uma outra possível solução com ideia parecida</summary>

#### Aprendendo um pouco mais

  Em caso de ter problema com TLE (o que não deve ocorrer) você pode optar por usar duas estruturas, sendo elas um vetor e um set.
- set: você guardará de forma ordenada decrescente todos os valores, essa estrutura não irá guardar itens duplicados;
- vetor: você guardará na posição do número do set quantas vezes aquele número apareceu.

Para entradas do exemplo abaixo

```
10
4
1
1
2
1
4
4
3
4
4
5
```

O resultado seria das nossas estuturas seria

<details>
  <summary>Visualizar Imagem</summary>
  <img src="https://github.com/RickelmeDias/CPLab/assets/43411893/14f1cfcf-c458-47cb-b7d0-6a55764053aa" alt="Imagem de um set com valores e um vector" />
</details>

Com isso facilmente poderia buscar do começo ao fim no set e comparar com quantas vezes esse valor apareceu no vetor.

- Veja um pouco mais sobre set:
  - [C++](https://www.geeksforgeeks.org/set-in-cpp-stl/)  
</details>
