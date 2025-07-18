#include <stdio.h>
#include <string.h>

int main(){
    int n;
    char direcoes[] = "XNLSO";
    while(1){
    scanf("%d",&n);
    if(n==0)break;
    char ordens[n];
    scanf("%s",&ordens);
    // norte,leste,sul,oeste - 1,2,3,4
    int atual=1;
    for (int i =0;i<n;i++){
        if(ordens[i]==68)atual+=1;
        else atual-=1;

        if(atual == 5)atual=1;
        else if(atual == 0)atual=4;
    }
    printf("%c\n",direcoes[atual]);
    
    }
    return 0;
}