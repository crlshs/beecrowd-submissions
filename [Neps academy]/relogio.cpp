#include <bits/stdc++.h>
using namespace std;

int main(){
    cin.tie(0)->sync_with_stdio(0);
    int h, m, s, a; cin >> h >> m >> s >> a;

    s += a;
    while (s >= 60){
        m++;
        s -= 60;
        if (m >= 60){
            m -= 60;
            h++;
        if (h > 23){
            h -= 24;
        } 
        }
    }
    cout << h << "\n" << m << "\n" << s << endl;
    return 0;
}