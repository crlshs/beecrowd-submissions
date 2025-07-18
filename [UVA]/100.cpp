#include <iostream>
using namespace std;

int main() {
    int i, j;
    while (cin >> i >> j) {
        int oi = i;
        int oj = j;

        if (i > j) swap(i, j);
        int maximum = 0;

        for (int k = i; k <= j; k++) {
            int c = 1;
            long long n = k;
            while (n != 1) {
                if (n % 2 == 0)
                    n /= 2;
                else
                    n = (n * 3) + 1;
                c++;
            }
            if (c > maximum) maximum = c;
        }

        cout << oi << " " << oj << " " << maximum << endl;
    }
    return 0;
}
