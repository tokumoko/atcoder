#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    int K, mod = pow(10, 9) + 7;
    cin >> K;
    vector<int> dp(K+1);
    if (K % 9 != 0){
        cout << 0 << endl;
        return 0;
    }
    dp[0] = 1;
    int i, l;
    for (i = 0; i< K+1; i++){
        if (i > 9) l = 9;
        else l = i;
        for(int j = i-l; j < i; j++){
            dp[i] += dp[j];
            dp[i] %= mod;
        }
    }
    cout << dp[K] << endl;
    return 0;
}