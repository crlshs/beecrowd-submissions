#include <iostream>
using namespace std;

bool verifica(int a, int b, int c, int d) {
    return (a + b == c + d) && (a + c == b + d);
}

int main() {
    int v[4];
    for (int i = 0; i < 4; i++) cin >> v[i];

    bool ok = false;

    ok |= verifica(v[0], v[1], v[2], v[3]);
    ok |= verifica(v[0], v[2], v[1], v[3]);
    ok |= verifica(v[0], v[3], v[1], v[2]);
    ok |= verifica(v[1], v[2], v[0], v[3]);
    ok |= verifica(v[1], v[3], v[0], v[2]);
    ok |= verifica(v[2], v[3], v[0], v[1]);

    cout << (ok ? "S" : "N") << endl;
    return 0;
}
