#include <bits/stdc++.h>
using namespace std;

int main () {
    int n; cin >> n;

    while (n--) {
        string s;
        cin >> s;

        s.erase(remove(s.begin(), s.end(), '.'),s.end());
        // string sem os pontos somente <><><>><<<> etc

        int contador = 0;
        bool achou = true;

        while (achou) {
            achou = false;
            string nova_s;

            for (int i = 0; i < s.size(); i++) {
                if (i < s.size()-1 && s[i] == '<' && s[i+1] == '>') {
                    contador++;
                    achou = true;
                    i++;
                }
                else nova_s += s[i];
            }
            s = nova_s;
        }
            cout << contador << endl;
        }
        return 0;
    }
