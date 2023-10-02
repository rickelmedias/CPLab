#include<bits/stdc++.h>

using namespace std;

int main() { 
  ios_base::sync_with_stdio(false);cin.tie(NULL);

  // Control Variables
  int leastPotion = 1000;
  int leastPotionPosition = -1;
  
  int N,H,X,currPotion;
  
  cin >> N >> H >> X;
  
  int n = N;  
  while (N--) {
    cin >> currPotion;
    
    if (currPotion + H == X) {
      leastPotion = min(leastPotion, currPotion);
      leastPotionPosition = abs(N-n);
      break;
    }
    
    if (currPotion + H > X) {
        if (leastPotionPosition == -1) {
            leastPotion = currPotion;
            leastPotionPosition = abs(N-n);
        }else{
            if (leastPotion + H > currPotion + H) {
                leastPotion = currPotion;
                leastPotionPosition = abs(N-n);
            }
        }
    }
  }
  
  cout << leastPotionPosition << endl;
}

