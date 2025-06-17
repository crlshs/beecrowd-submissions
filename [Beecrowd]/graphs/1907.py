def floodFill(matriz, start_l, start_c, cor):
    alterar = matriz[start_l][start_c]
    if alterar == cor:
        return

    pilha = [(start_l, start_c)]
    while pilha:
        l, c = pilha.pop()
        if (l < 0 or l >= len(matriz) or c < 0 or c >= len(matriz[0])):
            continue
        if matriz[l][c] != alterar:
            continue

        matriz[l][c] = cor

        pilha.append((l + 1, c))
        pilha.append((l - 1, c))
        pilha.append((l, c + 1))
        pilha.append((l, c - 1))

n, m = map(int, input().split())
coordenadas = set()
matriz=[]
for l in range(n):
    linha = list(input())

    for col in range(len(linha)):
        if (linha[col] == "."):
            coordenadas.add((l,col))

    matriz.append(linha)

numCor = 0
while (coordenadas):
    line,column = coordenadas.pop()
    if matriz[line][column] != '.':
        continue
    
    floodFill(matriz,line,column, str(numCor))
    numCor+=1

print(numCor)
