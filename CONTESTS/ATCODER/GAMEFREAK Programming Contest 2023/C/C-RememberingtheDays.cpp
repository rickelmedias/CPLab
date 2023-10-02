#include <bits/stdc++.h>

#define maxN 11

using namespace std;

vector<vector<int>> matrixAdj(maxN, vector<int>(maxN, 0));
vector<int> vis(maxN, 0);

int dfs(int N) {
    vis[N] = 1;
    
    int res=0;
    for (int i=1; i<=maxN; i++) {
        if (matrixAdj[N][i] > 0 && vis[i]==0) {
            res = max(res, matrixAdj[N][i]+dfs(i));
        } 
    }
    
    vis[N] = 0;
    return res;
}

int main() {

    int N, M, A, B, C;
    cin >> N >> M;
    
    for (int i=1; i<=M; i++) {
        cin >> A >> B >> C;
        matrixAdj[A][B] = C;
        matrixAdj[B][A] = C;
    }

    int longestPath = 0; 
    for (int n=1; n<=N; n++) {
        longestPath = max(longestPath, dfs(n));
    }
    cout << longestPath << endl;
 
    return 0;
}
