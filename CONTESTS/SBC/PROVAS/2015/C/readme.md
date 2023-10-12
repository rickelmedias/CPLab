
# **PROBLEMA C "TRI-DU"**

## **Resolução:**

Neste exercício precisamos verificar duas condições de acordo com as regras do jogo, que são elas:

### **1ª REGRA:**

Se as duas primeiras cartas forem iguais, a terceira deverá ser igual as demais para se formar um trio, sendo então capaz de vencer o jogo.

### **2ª REGRA:**

Em caso das duas primeiras cartas serem diferentes, a terceira deverá ser igual a uma das duas, maximizando a possiblidade de formar um duo, já que não é possível formar um tri.
O exercício em questão pode ser resolvido utilizando apenas condições If Else, e cabe ao desenvolvedor definir se a terceira carta será igual a primeira ou a segunda, de acordo com as condições do jogo.

### RESOLUÇÃO EM C++

``` C++
#include <iostream>
using namespace std;

int main() {
    int A, B;
    while (cin >> A >> B)
     {
        if (A == B)
        {
            cout << A << endl;
            // Ou cout << B <<endl;
        }
        else if (A > B) 
        {
            cout << A << endl;
        } 
        else //Terceira carta = B 
        {
            cout << B << endl;
        }
    }
    return 0;
}
```
