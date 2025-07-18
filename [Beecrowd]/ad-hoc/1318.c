#include <stdio.h>
#include <stdlib.h>

int compare(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}


int main(){
    while (1){
    int n,m;
    scanf("%d %d",&n,&m);
    if (n==0&&m==0){
        return 0;
        break;
    }
    int v[m];
    for (int i=0; i<m;i++){
        scanf("%d",&v[i]);
    }

    qsort(v, m, sizeof(int), compare);

    int erros=0;
    int atual = -1;
    int contado=0;
    for (int j=0;j<m-1;j++){
        if(v[j]!=atual){
            atual=v[j];
            contado=0;
        }

        if (v[j]>n){
            erros++;
        }
        if(v[j] == v[j+1] && contado == 0){
            contado=1;
            erros++;
        }
    }
    if(v[m-1] > n) erros++;
    printf("%d\n",erros);
}

    return 0;
}