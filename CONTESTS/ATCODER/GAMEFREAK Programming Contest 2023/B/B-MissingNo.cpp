#include <bits/stdc++.h>

#define FOR(x,n) for(int x=0;(x)<int(n);(x)++)
#define ____ ios_base::sync_with_stdio(0);cin.tie(0);

using namespace std;

typedef vector<int> vi;

int main() { ____
    
    int N, currValue;
    cin >> N;
    
    int i=0;
    vi Avec;
    
    // Inserting values sorted
    FOR(i, N) {
        cin >> currValue;
        // Find position to insert sorted
        auto it = lower_bound(Avec.begin(), Avec.end(), currValue);
        Avec.insert(it, currValue);
    }
    
    
    i=0;
    
    FOR(i, Avec.size()-1) {
        if (Avec[i+1] != Avec[i]+1)
            cout << Avec[i]+1 << endl;
    }

    return 0;
}
