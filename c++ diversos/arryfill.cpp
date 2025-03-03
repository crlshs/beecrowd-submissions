#include <iostream>
using namespace std;

int main() {

    int v; cin >> v;
    int arr[11];

    arr[0] = v;
    cout << "N[" << 0 << "] = " << arr[0] << endl;

    for (int i = 1; i <= 10; i++) {
        arr[i] = arr[i-1] * 2;
        cout << "N[" << i << "] = " << arr[i] << endl;
    }

    return 0;
}
