def vizinhar(matrix, linha, coluna):
    if linha < 0 or linha >= len(matrix): return 0
    if coluna < 0 or coluna >= len(matrix[0]): return 0
    return matrix[linha][coluna]

def contaminar(posicao, t, c):
    if (posicao == 0):
        return t, c+1
    elif (posicao == 1):
        return t, c-1
    elif (posicao == 2):
        return t+1, c
    elif (posicao == 3):
        return t-1,c
    return 0, 0

while (True):
    try:
        x, y = list(map(int, input().split()))
    except: break
    if (x == 0 and y == 0): break

    matriz = []
    coordenadas = set()

    for l in range(x):
        linha = list(input())

        for col in range(len(linha)):
            if (linha[col] == "T"):
                coordenadas.add((l,col))

        matriz.append(linha)

    visitados = set()

    while (coordenadas):
        t,c = coordenadas.pop()
        if ((t,c) in visitados): continue

        visitados.add((t,c))

        adjacentes = [
        vizinhar(matriz, t, c+1),
        vizinhar(matriz, t, c-1),
        vizinhar(matriz, t+1, c),
        vizinhar(matriz, t-1, c)
        ]

        for posicao,k in enumerate(adjacentes):
            if k == 'A':
                line, column = contaminar(posicao, t, c)

                matriz[line][column] = "T"
                if ((line,column) not in visitados):
                    coordenadas.add((line,column))

    for linha in matriz:
        print("".join(linha))
    print()
