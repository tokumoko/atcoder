#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i = 0; i < n; i++)
#define vi vector<int>
using ll = long long;

int main(){
    int N, i, ans = 0;
    cin >> N;
    vi A(N);
    rep(i, N) cin >> A[i];
    rep(i, N) ans += A[i];
    cout << ans << endl;
}