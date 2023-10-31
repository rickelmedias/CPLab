# Problema M - Máquina de Café
###### [Caminho para Beecrowd](https://www.beecrowd.com.br/judge/pt/problems/view/2670)

Uma abordagem direta e eficaz para resolver esse problema, dada a pequena quantidade de entradas (apenas três), é calcular todas as possíveis combinações. Essa abordagem é viável porque sabemos o número exato de entradas e ele é bastante baixo.

Para resolver o problema, primeiro identificamos todas as combinações possíveis de entrada, e então calculamos o tempo necessário para um funcionário se deslocar entre os andares A, B e C. É importante notar que, devido ao tempo de deslocamento, são necessários 2 minutos para que um funcionário se mova de um andar para outro, uma vez que ele deve retornar ao seu andar original após o deslocamento.

Em resumo, a solução envolve:
1. Listar todas as combinações possíveis das três entradas.
2. Para cada combinação, calcular o tempo total necessário para que os funcionários se desloquem entre os andares A, B e C, levando em consideração os 2 minutos extras para o retorno ao andar de origem.

Dessa forma, você poderá determinar o tempo mínimo necessário para que todos os funcionários se desloquem entre os andares com base nas três entradas disponíveis.

<details>
  <summary>Imagem Explicativa da Solução Proposta</summary>
  <img src="https://github.com/RickelmeDias/CPLab/assets/43411893/938e0815-d0ff-48b7-a097-1eb257d88468" />
</details>
