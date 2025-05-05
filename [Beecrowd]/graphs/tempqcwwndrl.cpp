#include <iostream>
using namespace std;

int main() {
    int a, b, c, d; cin >> a >> b >> c >> d;
    if ((a+d) == (c+b) && (a+c) == (b+d)) {
        cout << "S" << endl;
    } else {
        cout << "N" << endl;
    }

    return 0;
}