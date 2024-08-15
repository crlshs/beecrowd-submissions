#include <bits/stdc++.h>
using namespace std;

int main(){
    int n; cin >> n;
    int sequencia[n]; 
    
    for (int i = 0; i < n; i++)
    {
    cin >> sequencia[i];
    }

    int vezes = 0;

    for (int i = 0; i <= n-3; i++)
    {
        if (sequencia[i] == 1 && sequencia[i+1] == 0 && sequencia[i+2] == 0)
        {
            vezes++;
        }
    }
    cout << vezes << endl;

    return 0;
}
