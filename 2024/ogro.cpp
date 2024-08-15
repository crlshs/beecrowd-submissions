#include <bits/stdc++.h>
using namespace std;

int main(){
    int e, d; cin >> e >> d;

    int res = e + d;
    if (e < d) res = 2 * (d - e);

    cout << res << endl;
}