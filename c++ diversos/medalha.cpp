#include <bits/stdc++.h>
using namespace std;
int main(){
    int a, b, c; cin >> a >> b >> c;

    int original[3] = {a, b ,c};
    int copia[3] = sort(original[0], original[-1]);

    cout << copia << endl;
    return 0;
}