# Resolução
Para resolver esse problema, primeiro recebemos como entrada o número de interações, o valor mínimo de vencedores desejado e todas as pontuações obtidas. Em seguida, utilizamos o algoritmo de ordenação Merge Sort para organizar as pontuações em ordem crescente.

Uma vez que as pontuações estão ordenadas, podemos encontrar o vencedor mínimo acessando o elemento no índice minVencedor - 1 do array ordenado. Em seguida, usamos um loop "for" para iterar pelas pontuações no array e somamos 1 ao contador enquanto a pontuação atual for menor ou igual à pontuação limite desejada. Quando encontramos uma pontuação maior que a pontuação limite, interrompemos o loop e imprimimos o contador, que representa o número de vencedores atingidos.

A complexidade assintótica desse algoritmo é O(n*log(n)), devido ao uso do Merge Sort para ordenar as pontuações. Isso significa que o desempenho do algoritmo cresce de forma logarítmica em relação ao tamanho da entrada, o que o torna eficiente para lidar com grandes conjuntos de dados.
