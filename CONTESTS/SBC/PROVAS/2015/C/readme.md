# Problema C - Tri-Du
###### [Caminho para BeeCrowd](https://www.beecrowd.com.br/judge/pt/problems/view/1933)

Neste exercício precisamos verificar duas condições de acordo com as regras do jogo, que são elas:

##### **1ª REGRA:**

Se as duas primeiras cartas forem iguais, a terceira deverá ser igual as demais para se formar um trio, sendo então capaz de vencer o jogo.

##### **2ª REGRA:**

Em caso das duas primeiras cartas serem diferentes, a terceira deverá ser igual a maior carta entre as das duas, maximizando a possiblidade de formar um duo, já que não é possível formar um tri.
O exercício em questão pode ser resolvido utilizando apenas condições If Else, e cabe ao desenvolvedor definir se a terceira carta será igual a primeira ou a segunda, de acordo com as condições do jogo.

##### LÓGICA DA SOLUÇÃO

| Carta A | Carta B | Carta C                                  |
|---------|---------|------------------------------------------|
| 10      | 7       | Mostrar maior entre 10 e 7, no caso o 10 | 
| 2       | 2       | Mostrar 2                                |

É possível usar um if else para comparar quem é maior entre 10 e 7 na hora de mostrar, ou também pode usar a função **max** em c++, que é responsável por obter dois valores em seus paremetros e já retornar o maior entre eles, exemplo: `a = max(10,7)` ou `a = max(7,10)` é dizer que `a = 10`. O **max** é bastante conhecido, ao buscar poderá encontrar o max para diversas linguagens de programação.

- [max() em Java](https://www.geeksforgeeks.org/java-math-max-method-examples/)
- [max() em C++](https://www.geeksforgeeks.org/stdmax-in-cpp/)
- [max() em Python](https://www.geeksforgeeks.org/python-max-function/)
