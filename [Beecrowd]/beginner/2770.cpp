#include <iostream>
using namespace std;

int main() {
    int x,y,m;
    while(cin >> x >> y >> m) {
        int limite = x*y;

        for (int i=0;i < m; i++) {
            int xi, yi;
            cin >> xi >> yi;
            if (cin.fail()) break;

            cout << ((xi * yi) > limite ? "Nao" : "Sim") << endl;
        }
    }

    return 0;
}