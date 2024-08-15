#include <bits/stdc++.h>
using namespace std;

int main(){
    cin.tie(0)->sync_with_stdio(0);

    int idade, um, dois;
    cin >> idade >> um >> dois;

    int tres = idade - (um + dois);

    cout << max(max(um, dois), tres) << endl;
}