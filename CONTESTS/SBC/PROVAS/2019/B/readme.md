# Problema B - Bobo da Corte
###### Caminho para Beecrowd
Para o exercício "Bobo da corte" da lista de 2019 a lógica utilizada foi a seguinte:

A primeira entrada $N$ é a quantidade de bobos da corte que estão concorrendo a vaga, para obter a quantidade de votos será utilizado um for de $i = 1$ até $i < N$;

Temos duas condicões que de vitória para Carlos: 
1. Se o primeiro candidato $Carlos$ (i==1) tiver o maior numero de votos ele ganhará;
2. Se todas as entradas de quantidades de votos forem iguais ao de 'Carlos', então ele também ganhará.

Ou seja, 'Carlos' (i=1) só perderá se alguma entrada da quantidade de votos for maior que a dele, para obter e comparar com Carlos outras entradas de votos utilizaremos a variável $v$, sendo assim $v > Carlos$ então ele perderá.
