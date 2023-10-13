# Problema K - Katmandu
###### [Caminho para Codeforces](https://codeforces.com/gym/103388/problem/K)
Este exercício se trata da verificação se podemos dormir por um período ininterrupto de tempo ou não num voo. Nós recebemos os valores de quato precisamos dormir (T), a duração do voo (D) e quantas interrupções teremos durante esse voo (M). Após isso, se M for maior que 0, receberemos M valores crescentes indicando o momento que seremos interrompidos.

Para resolver este exercício, eu usei a seguinte lógica:
Enquanto recebemos cada momento indicando a interrupção, nós podemos calcular quantos minutos tivemos até este momento subtraindo o valor recebido pelo valor anterior recebido, e guardando o resultado deste cálculo em uma variável `maxPeriodoDormindo` caso ele seja o maior encontrado até agora.

Após receber todos os momentos de interrupção e calcularmos quantos minutos tivemos do último momento até o fim da duração do voo, nós podemos simplesmente verificar se o valor da variável `maxPeriodoDormindo` foi maior ou igual o valor T mínimo que precisamos, imprimindo "Y" caso sim ou "N" caso não.
