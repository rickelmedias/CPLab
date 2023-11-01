# Problema I - Interceptando Informações
###### [Caminho para Beecrowd](https://www.beecrowd.com.br/judge/pt/problems/view/3432)

A ideia é basicamente receber uma sequencia de 8 valores e se um deles for 9 deverá mostrar `'N'`, caso contrario se nenhum dos valores for 9, deverá mostrar `'S'`.

Um lógica bastante simples para resolver, você pode fazer uma variável (char) que contenha `'S'` por padrão, e ao fazer um loop para ler os 8 valores você pode verificar a condição `valor == 9`, se essa condição for verdade você pode mudar a variável do tipo char que criamos antes de entrar no loop para `'N'` e dar um `break` no loop, em seguida fora do loop mostrar essa variável.