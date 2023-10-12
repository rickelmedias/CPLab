
# **PROBLEMA A "ANDANDO NO TEMPO"**

## **Resolução:**

Neste exercício, o usuário vai definir os valores para as fichas A,B e C.
Um detalhe a ser observado é que a ordem das fichas não determina o curso da viagem, pois o usuário pode viajar com a ficha A e retornar com a C, sem utilizar a B por exemplo, ou ir ao passado com a C e voltar com a B, existem várias combinações/possibilidades entre as fichas!
Outro detalhe a ser observado, é que o usuário pode somar as fichas para viajar para o futuro ou para o passado, podendo ou não escolher utilizar a ficha restante. Por exemplo: viajar ao futuro com as fichas A e B e retornar com a C, ou viajar ao passado com a B e C e ir ao futuro com a A.
Uma vez compreendido este conceito, basta programarmos as condições em que uma ficha anule a outra, pois significa que o usuário viajou para o passado/futuro e retornou ao presente, pois o a diferença entre os anos viajados seriam zero, lembrando que temos condições de viagem utilizando duas fichas ou utilizando as três. Importante ter em mente que o usuário só volta ao presente caso as diferenças de anos entre as fichas utilizadas se anulem!

**ENTRADA:** A entrada consiste de uma linha contendo os valores dos três créditos A, B e C (1 <= A, B, C <= 1000).

**SAÍDA:** Seu programa deve imprimir uma linha contendo o caractere “S” se é possível viajar e voltar para o presente, ou “N” caso contrário.

Exemplo de Entrada   | Exemplo de Saída
-------------------- | ----------------
22 5 22              |       S
31 110 79            |       S
49 8 7               |       N

### **SCRIPT EM C++**

``` C++
#include <iostream>
using namespace std; 
        
int main() {
    
    int a=0;
    int b=0;
    int c=0;

    cin>>a>>b>>c;
    //Condição apenas ida e volta
    if(a-b ==0 || a-c ==0 || b-c ==0)
    {
        cout<<"S"<<endl;
    }

    //Condição utilizando as três fichas
    else if(a+b-c ==0 ||b-a+c ==0 || c-a+b ==0)
    {
        cout<<"S"<<endl;
    }
    //Condição utilizando as três fichas
    else if(a-b-c ==0 ||b-a-c ==0 || c-a-b ==0)
    {
        cout<<"S"<<endl;
    }
    else
    {
        cout<<"N"<<endl;
    }
    return 0;
}
```
