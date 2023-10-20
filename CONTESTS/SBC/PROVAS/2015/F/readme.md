# Problema F - FATORIAL

Neste exercício, precisamos mostrar na tela a menor quantidade de números fatorados onde a soma entre eles sejam iguais a N e, para isso, precisamos primeiramente ter esses números já fatorados. Portanto, o primeiro passo será receber o valor de N e fazer sua fatoração. 
Um detalhe importante a ser considerado é o fato de que para os números 0 e 1, sua fatoração será igual a 1.
Uma vez criado uma função para fatorar o número, precisamos criar um vetor cujo objetivo é armazenar os valores fatorados, pois para descobrirmos quais números compõem a soma resultante de N, precisamos da lista de números fatorados para descobrirmos a menor quantidade de números fatoriais.
Com o vetor criado, precisamos criar um loop onde chamamos a função de fatorar passando como parâmetro o valor de N. Para cada execução, o resultado desta condição será um número fatorado na posição(i), armazenado no vetor.
Por fim, para definirmos a menor quantidade de números a serem somados, criamos outro loop onde percorremos o vetor em ordem decrescente, subtraindo o valor de N pelo número fatorado e colocando em um contador, pois ao percorrer o vetor em ordem decrescente estamos maximizando a possibilidade de encontrarmos a menor quantia.
Ao final do script basta imprimirmos a variável do contador.
