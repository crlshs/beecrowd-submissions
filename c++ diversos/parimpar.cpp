#include <iostream>
using namespace std;
int main(){
    cin.tie(0)->sync_with_stdio(0);
    int x; cin >> x;

    string res = "impar";
    if (x % 2 == 0) res = "par";
    cout << res << endl;
}