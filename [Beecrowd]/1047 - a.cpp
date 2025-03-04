#include <iostream>
using namespace std;
int main() {
    int sh, sm, eh, em;
    cin >> sh >> sm >> eh >> em;

    int diftotal = (((60 * eh)+ em) - ((60 * sh) + sm));

    int hora;
    if (diftotal >= 0) {
        if (diftotal < 60 && diftotal > 0) {
            hora = 0;
        }
        else if (diftotal >= 60) {
            hora = int(diftotal / 60);
            diftotal -= 60*hora;
        }
        else if (diftotal == 0) {
            hora = 24;
            diftotal = 0;
        }
    }

    else if (diftotal <= 0){
        if (diftotal > -60) {
            hora = 23;
            diftotal = 60 + diftotal;
        }

        else if (diftotal <= -60) {
            diftotal*=-1;
            hora = 24 - (int(diftotal/60));
            diftotal -= 60 * (int(diftotal/60));
            if (diftotal > 0) {
                hora -= 1;
                diftotal = 60 - diftotal;
            }
        }

    }

    cout << "O JOGO DUROU " << hora << " HORA(S) E " << diftotal << " MINUTO(S)" << endl;

    return 0;
}