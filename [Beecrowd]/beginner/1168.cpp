#include <iostream>
using namespace std;

int countLeds(string num) {
    int count = 0;
    for (char c : num) {
        switch (c) {
            case '1':
                count += 2;
                break;
            case '0':
            case '9':
            case '6':
                count += 6;
                break;
            case '2':
            case '3':
            case '5':
                count += 5;
                break;
            case '4':
                count += 4;
                break;
            case '7':
                count += 3;
                break;
            case '8':
                count += 7;
                break;
        }
    }
    return count;
}

int main() {
    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        string num;
        cin >> num;
        cout << countLeds(num) << " leds" << endl;
    }

    return 0;
}
