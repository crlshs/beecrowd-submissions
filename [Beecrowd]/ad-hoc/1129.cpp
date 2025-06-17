#include <iostream>
#include <vector>

using namespace std;

int main(){
    int n = -1;
    while (n != 0){
        cin >> n;
        if (n==0) return 0;

        for (int i = 0; i<n;i++){
            int a,b,c,d,e;
            cin >> a >> b >> c >> d >> e;
            vector<int> respostas = {a,b,c,d,e};

            bool achou = false;
            int res = -1;

            for (int j = 0; j<5; j++){
                if(respostas[j]<=127){
                    if(not achou){
                        res = j;
                        achou = true;
                    }else{
                        res = -1;
                        break;
                    }
                }
            }
            string letras = "ABCDE";
            if (res == -1) cout << "*" << endl;
            else cout << letras[res] << endl;
        }
    }
    return 0;
}