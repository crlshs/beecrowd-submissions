#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
    int n = -1;
    while(cin >> n){
        if (n == 0) return 0;
        vector<int> ordem;
        for (int i = 0; i<n;i++){
            int x;
            cin >> x;
            ordem.push_back(x);
        }
        int maria = count(ordem.begin(),ordem.end(),0);
        int joao = count(ordem.begin(),ordem.end(),1);

        cout << "Mary won " << maria << " times and John won "<< joao << " times" << endl;
    }
    return 0;
}