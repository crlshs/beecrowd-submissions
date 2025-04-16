#include <iostream>
using namespace std;

#define out(n) cout << "N[" << n << "] = " << arr[n] << endl;

int main() {

    int v; cin >> v;
    int arr[10];

    arr[0] = v;
    out(0);

    for (int i = 1; i < 10; i++) {
        arr[i] = arr[i-1] * 2;
        out(i);
    }

    return 0;
}
