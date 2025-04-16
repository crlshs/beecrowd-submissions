#include <iostream>
using namespace std;

int main() {
    int n; cin >> n;

    for (int i = 0; i < n; i++) {
        string s; cin >> s;
        int k; cin >> k;
        string res;

        for (char c :s) {
            if (c - k < 'A') {
                res += char(c-k+26);
            } else {
                res += char(c -k);
            }
        }
        cout << res << endl;
    }
    return 0;
}