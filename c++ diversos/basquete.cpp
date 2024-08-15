#include <bits/stdc++.h>
using namespace std;

int main() {
    int d; cin >> d;
    int res = 0;

    if (d <= 800) res = 1;
    else if (d > 800 && d <= 1400) res = 2;
    else if (d > 1400 && d <= 2000) res = 3;

    cout << res << endl;
    return 0;
}