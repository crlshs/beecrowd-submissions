#include <bits/stdc++.h>

using namespace std;

int main(){
    vector<int> vetor {};

    for(int i = 0; i < 6; i++){
        int x; cin >> x;
        vetor.push_back(x);
    }

    int aux;
    for(int j = 0; j < vetor.size(); j++){
        vetor[j] = vetor[vetor.size() - j - 1];
    }

    for(int i = 0; i < vetor.size(); i++){
        cout << vetor[i] << " ";
    }

    return 0;
}