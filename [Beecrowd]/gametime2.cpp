#include <iostream>
using namespace std;
int main() {
    int sh, sm, eh, em;
    cin >> sh >> sm >> eh >> em;

    int start = sh * 60 + sm;
    int end = eh * 60 + em;
    int diftotal = end - start;

    if (diftotal <= 0) diftotal += 24 * 60;

    int hora = diftotal / 60;
    int minuto = diftotal % 60;

    cout << "O JOGO DUROU " << hora << " HORA(S) E " << minuto << " MINUTO(S)" << endl;

    return 0;
}