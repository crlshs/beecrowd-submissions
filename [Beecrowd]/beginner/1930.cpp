#include <bits/stdc++.h>
using namespace std;

int main() {
    int v[4];
    cin >> v[0] >> v[1] >> v[2] >> v[3];

    sort(v, v + 4);

    int total = ((v[0]-1 + v[3])-2)+v[1]+v[2];

    cout << total << endl;

    return 0;
}