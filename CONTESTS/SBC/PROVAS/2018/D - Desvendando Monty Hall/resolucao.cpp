#include<bits/stdc++.h>

using namespace std;

int main() {
  int ganhou = 0, carro, test;

  cin >> test;

  for(int i = 0; i<test; i++) {
    cin >> carro;
    if (carro > 1) ganhou++;
  }

  cout << ganhou << endl;
  return 0;
}