#include <bits/stdc++.h>
using namespace std;

int main () {
    int n;
    int cidade = 0;
    while (cin >> n && n != 0) {
        cidade++;
        vector<pair<int, int>> v;
        int somax = 0;
        int somay = 0;

        for (int i = 0; i < n; i++) {
            int x, y; cin >> x >> y;

            somax += x;
            somay += y;

            int consumo_por_pessoa = floor((float)y / x);
            
            bool found = false;
            for (auto& p : v) {
                if (p.second == consumo_por_pessoa) {
                    p.first += x;
                    p.second = floor((float)(p.second * p.first) / p.first);
                    found = true;
                    break;
                }
            }

            if (!found) {
                v.push_back({x, consumo_por_pessoa});
            }
        }

        float media = (float)somay / somax;

        // função lambda para ordenação por consumo por pessoa
        sort(v.begin(), v.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
            return a.second < b.second;
        });

        if (cidade != 1) cout << "\n";

        cout << "Cidade# " << cidade << ":\n";
        
        for (int i = 0; i < v.size(); ++i) {
            printf("%d-%d", v[i].first, v[i].second);
            if (i != v.size() - 1) {
                printf(" ");
            }
        }


        cout << "\nConsumo medio: " << fixed << setprecision(2) << media << " m3.\n";
    }

    return 0;
}
