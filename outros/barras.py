n = int(input())
lista = list(map(int,input().split()))
k = max(lista)
matriz = []

for i in range(max(lista)):
    linha=[]
    for j in lista:
        if (j <k):
            linha.append(0)
        else:
            linha.append(1)
    matriz.append(linha)
    k-=1

for i in matriz:
    for j in i:
        print(j, end=" ")
    print()