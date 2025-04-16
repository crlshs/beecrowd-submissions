#include <iostream>
using namespace std;

int main() {
    int n; cin >> n;

    for (int i = 0; i < n; i++) {
        int x;
        bool prime = true;
        cin >> x;

        for (int j = 2; j < x; j++) {
            if (x % j == 0) {
                cout << x << " nao eh primo"<< endl;
                prime = false;
                break;
            }
        }
        if (prime) {
            cout << x << " eh primo" << endl;
        }
    }

    return 0;
}