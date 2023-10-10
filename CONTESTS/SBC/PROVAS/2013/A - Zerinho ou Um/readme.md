# Questão A - Zerinho ou Um

[Exercício no Beecrowd](https://www.beecrowd.com.br/judge/pt/problems/view/1467)


- # Resolução
    --
    
    A resolução para esse problema é bem simples, pois a mesma será feita utilizando uma cadeia de **`if`** e **`else if`**. Deve-se considerar sempre aquele que for diferente dos demais como o ganhador e imprimir a letra correspondente. Caso não haja um ganhador, deverá ser mostrado um '*'.
    
    Segue uma tabela lógica para melhor entendimento:
    


    | se A for diferente de B e C | imprima A |
    | --- | --- |
    | se B for diferente de A e C | imprima B |
    | se C for diferente de A e B | imprima C |
    | caso contrário | imprima * |
    


    Vale a pena ressaltar uma situação que ocorreu dentro do BeeCrowd:
    
    O exercício dentro do BeeCrowd considera múltiplas entradas em uma única execução, ou seja, vão ocorrer múltiplos jogos e terá que printar o resultado de cada jogo. Desse modo, ele inclui o EOF (End of File) como uma restrição da entrada. Isso significa que, precisará colocar uma lógica onde detectará uma condição final de entrada para assim encerrar o programa.  
    
    Em suma, o EOF é geralmente usado para indicar para o programa ou sistema operacional que não há mais dados a serem lidos, evitando tentativas de ler dados que não existem, caso o contrário, poderia levar a problemas ou travamentos no programa.
    
    Uma forma de resolver esse problema foi através de um loop while que irá dar um break a partir do momento que, ocorrer o EOFError ou então quando não tiver mais linhas de entrada:
    
    ```python
    while True:
        try:
            # Tenta ler uma linha de entrada
            entrada = input()
            
            # Se não houver mais entrada (EOF), encerra o loop
            if not entrada:
                break
    
    		"""
    		Lógica do Programa
            """
    
    	except EOFError:
            # Trata a exceção de EOF, se ocorrer
            break
    ```