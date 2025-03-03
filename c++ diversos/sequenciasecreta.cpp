#include <iostream>
using namespace std;

int main() {
    int n; cin >> n;
    int sequencia[n];

    int seqAtual = 1;
    int maiorSeq = 0;

    for (int i = 0; i < n; i++) {
        cin >> sequencia[i];

        if (i > 0) {
            int atual = sequencia[i];
            int anterior = sequencia[i - 1];

            if (atual != anterior){
                seqAtual += 1;
                cout << "aaa" << endl;
            }
            else{
                cout << "bbb" << endl;
                seqAtual = 1;
            }
        }
        if (seqAtual > maiorSeq) maiorSeq = seqAtual;
    }

    cout << maiorSeq << endl;
    return 0;
}