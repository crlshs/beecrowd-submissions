#include <bits/stdc++.h>
using namespace std;

int main(){
    cin.tie(0)->sync_with_stdio(0);
    int total, marinheiros; cin >> total;
    cin >> marinheiros;
    
    cout << 2 * (total/(marinheiros + 2)) << endl;

}