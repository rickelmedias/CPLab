# Questão A - Volta
###### [Exercício no BeeCrowd](https://www.beecrowd.com.br/judge/pt/problems/view/1708)

Para ajudar a resolver esse exercício, é útil montar uma tabela relacionando o tempo de cada carro na entrada e o número total de voltas fornecido na saída, encontrados nos exemplos do exercício, essa tabela permite determinar a volta em que a diferença de tempo entre os carros se torna maior ou igual ao tempo gasto pelo carro mais lento. Isso é feito multiplicando o tempo base, em segundos, de cada carro pelo número de voltas.

Segue um exemplo:

| n° de Voltas | 1° | 2° | 3° | 4° |
| --- | --- | --- | --- | --- |
| Carro mais rápido $(C1)$ | 5 | 10 | 15 | 20 |
| Carro mais lento $(C2)$ | 7 | 14 | 21 | 28 |
| Diferença de Tempo $(C2 - C1)$ | 2 | 4 | 6 | 8 |

A saída esperada para as entradas 5 e 7 é “4”, exatamente onde a diferença de tempo (8 segundos) foi maior que o tempo que o carro mais lento leva para percorrer uma volta (7 segundos), essa diferença representa o tempo que o carro mais lento levará para alcançar o carro mais rápido. Quando essa diferença se torna maior que o tempo necessário para uma volta completa na pista, isso indica que o carro mais rápido já ultrapassou o carro mais lento em uma ou mais voltas.

Desse modo, para solucionar o problema, será necessário colocar a operação:

$$C2 * n - C1 * n$$

Onde $C2$ representa o carro mais lento, o $C1$ o carro mais rápido e o $n$ o número de voltas. Esse valor pode ser guardado em uma variável, aguardando até o momento em que o resultado será maior ou igual ao valor do carro mais lento definido na entrada (nesse caso $7$). Até que isso ocorra, o valor do número de voltas será incrementado em mais 1, partindo do valor 1, ou seja, $n = 1$. Quando satisfazer a condição de:

$$C2 * n - C1 * n \geq C2$$
