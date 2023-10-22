# Problema K - Katmandu
###### [Caminho para Codeforces](https://codeforces.com/gym/103388/problem/K)

Este exercício se trata da verificação se podemos dormir por um período ininterrupto de tempo ou não num voo. Nós recebemos os valores: 

- **T**: quanto precisamos dormir;
- **D**: duração do voo;
- **M**: quantas interrupções teremos durante esse voo (M). 

Após isso, 

Se M for igual a 0, então iremos verificar se o tempo que precisamos dormir (T) é menor ou igual ao tempo de voo (D).
- Se o tempo que precisa dormir for menor ou igual ao tempo de voo: **Y**
- Se o tempo que precisa dormir for maior que o tempo de voo: **N**

Se M for maior que 0, receberemos M valores crescentes indicando o momento que seremos interrompidos.

Para resolver este exercício, eu usei a seguinte lógica:

1. Enquanto recebemos cada momento indicando a interrupção, nós podemos calcular quantos minutos tivemos até este momento subtraindo o valor recebido pelo valor anterior recebido, e guardando o resultado deste cálculo em uma variável `maxPeriodoDormindo`, caso ele seja maior que o valor anterior de `maxPeriodoDormindo`, pois isso indica que achamos um intervalo maior de perioro que a pessoa dormiu;
2. Após receber todos os momentos de interrupção, teremos na variavel `maxPeriodoDormindo` o maior intervalo de tempo seguido que conseguimos dormir. Dessa forma podemos simplesmente verificar se o valor da variável `maxPeriodoDormindo` é maior ou igual o valor **T** (tempo mínimo que precisamos dormir), imprimindo "Y" caso sim ou "N" caso não.
