#include <bits/stdc++.h>
using namespace std;

int main(){
    int x, y; cin >> x >> y;
    int dif = y - x;
    int z = y + dif;

    cout << max(y, z) << endl;
}
