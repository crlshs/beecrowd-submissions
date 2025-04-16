#include <iostream>
using namespace std;

int mdc(int a, int b) {
    // algoritmo de euclides....

    int resto;
    while ((a%b) > 0) {
        resto = a % b;
        a = b;
        b = resto;
    }
    return b;
}

int main () {
    int n; cin >> n;

    for (int i = 0; i < n; i++) {
        int a, b; cin >> a >> b;
        cout << mdc(a, b) <<
        endl;
    }

    return 0;
}