# Problema A - Revisão de Contrato
###### [Caminho para Beecrowd](https://www.beecrowd.com.br/judge/pt/problems/view/1120)

A lógica para solução do problema é bastante simples a partir do momento que você entende a lógica e conhece de manipulação de strings.

Nesse caso vamos usar o replace, que é uma função comumente encontrada nas linguagens de programação que nos permite trocar uma letra por outra, exemplo em pseudocódigo:

```
my_text = "Hello World";
my_text = my_text.replace("l", "3"); # Resultado: "He3lo World"
my_text = my_text.replaceAll("l", "3"); # Resultado: "He33o Wor3d"
```

Algumas linguagens de programação possuem um replace que troca todas as letras de uma vez, enquanto outras proporcionam um replaceAll para isso, de qualquer forma vale fazer a pesquisa sobre a que está utilizando.

Outras linguagens como C++, possuem uma função pronta para remover caracteres recorrentes, pois o replace pode reclamar quando tiver uma tentativa de replace por "vazio", ex: `''`, como o [remove_copy](https://stackoverflow.com/questions/3882304/replace-remove-character-in-string).

Sabendo disso, minha solução foi fazer um loop que recebia respectivamente os dados de $D$ e $N$ até que ambos fossem igual a zero, ou seja, a condição de parada desse loop é ambos ser zero, isso pode ser entendido no trecho:

> "O ultimo caso de teste é seguido por uma linha que contém apenas dois zeros separados por espaços em branco."

Dessa maneira sabemos que o programa é finalizado quando vier `0 0`.

Caso contrário, se o programa não for finalizado, iremos aplicar nosso conhecimento e lógica, que é:

0. Supondo que recebemos `9 "1931839"`, vamos ...
1. Certificar de que estamos recebendo os número como texto (strings)
    - Ex: `O número 1931839 deve ser "1931839"`  
2. Trocar todos os valores iguais a "D" por vazio ""
    - Ex: `"1931839".replace(D,"")`, ou seja, D é 9, entrão ficaria: `13183`
3. Mostrar o valor: `13183`

**É importante dar atenção as exceções**, são duas:
1. Quando o valor possui apenas zeros, ou seja, `"000000"` deverá mostrar apenas `"0"`
2. Quando o valor possui zeros a esquerda, eles não devem ser mostrados, exemplo: `00400`, deverá mostrar apenas `400`

>Lembre-se que se você estiver utilizando uma linguagem como c++ é importante entender que char são diferentes de strings, enquanto char é `'C'`, string pode ser um texto, reproduzido por: `"Coração`, então na hora de comparar ou remover sempre que for um a um deverá ser char a char, exemplo na palavra acima:  `'C' == 'C'`, `'C' == 'o'`, `'C' == 'r'`,  `'C' == 'a'`, `...`.


<details>
 <summary>Travou e não consegue resolver? Veja essas dicas.</summary>

 **Dica 1.**
 Em python você poderá transformar o texto com os replaces para inteiro, isso fará remover os zeros a esquerda e também já irá corrigir os multiplos zeros para um único zero quando for mostrar, veja:

 ```
 string => 0000 ------> int => 0
 string => 0040 ------> int => 40
 ```
 **Dica 2.** 
 Em python você poderá remover os zeros a esquerda utilizando funções prontas, como o `lsptrip`:

 ```py
    res = "000400".lstrip("0")
    print(str(res))                 # Output: 400
 ```

 **Dica 3.**
 Em outras linguagens caso não seja interessante aplicar as dicas anteriores, você pode fazer um loop saindo do primeiro char da string até o úlitmo e só mostrar os número a partir do momento que aparecer um char diferente de zero, pois enquanto aparecer zero desde o primeiro char, isso indica que são zeros a esquerda. 
 
 Se nunca aparecer um char diferente de zero, então dentro do loop você não irá mostrar nada, ou seja, sua saída para `000` será nada ` ` ao invés de `0`, então entra ai uma outra tratativa.
</details>