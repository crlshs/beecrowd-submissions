#include <bits/stdc++.h>
using namespace std;

string tautograma(string s) {
    char letra = tolower(s[0]);

    for (int i = 0; i < s.size(); i++) {
        if (s[i] == ' ' && i+1 < s.size()) {
            if (tolower(s[i+1]) != letra) return "N";
        }
    }
    return "Y";
}

int main () {
    string s;

    while (getline(cin, s) && s!= "*") {
        cout << tautograma(s) << endl;
    }

    return 0;
}