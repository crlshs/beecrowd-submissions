#include <iostream>
using namespace std;

int main() {
    int x; cin >> x;
    int total = 1;

    for (int i = 1; i < x; i++){
        total *= (x-i);
    }

    cout << total*x << endl;
    return 0;
}