# Problema B - Bobo da Corte

Para o exercício "Bobo da corte" da lista de 2019 a lógica utilizada foi a seguinte:
A primeira entrada 'N' é a quantidade de bobos da corte que estão concorrendo a vaga;
para a quantidade de votos sera introduzido um for de i = 1 até i < N;
temos duas condicões que podem ser quebradas e a partir disso utilizar apenas uma: a primeira será se o primeiro candidato 'Carlos' (i==1) tiver o maior numero de votos ele ganhará e a segunda acontecerá se todas as entradas de quantidades de votos forem iguais, 'Carlos' também ganhará. Ou seja, 'Carlos' (i=1) só perderá se alguma entrada da quantidade de votos for maior que a dele, para as outras entradas de votos utilizaremos a variável 'v', sendo assim v > Carlos.

