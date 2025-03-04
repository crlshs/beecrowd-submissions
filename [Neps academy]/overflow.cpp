#include <iostream>
using namespace std;

int main(){
    cin.tie(0)->sync_with_stdio(0);
    int max, a, b; cin >> max;
    string conta;
    cin >> a >> conta >> b;
    
    int res = 0;
    if (conta == "+") res = a + b;
    else res = a * b;

    if (res > max) cout << "OVERFLOW";
    else cout << "OK";
    
    return 0;
}
