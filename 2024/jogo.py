nq = list(map(int, input("").split()))
matriz = [[2] * (nq[0]+2)]

for i in range(nq[0]):
    linha = []
    linhap = list(map(str, input("").split()))
    for i in linhap:
        for j in i:
            linha.append(int(j))
    
    linha.insert(0, 2)
    linha.insert(nq[0]+1, 2)
    matriz.append(linha)
matriz.append([2] * (nq[0]+2))
# print(matriz)

# 2 2 2 2 2
# 2 0 0 0 2
# 2 0 0 0 2
# 2 0 0 0 2
# 2 2 2 2 2

# repetir isso Q vezes
for i, linha in enumerate(matriz):
    if i <= nq[0]:
        for j, val in enumerate(linha):
            if j <= nq[0]:
                vizinhas = [[matriz[i+1][j]],
                            [matriz[i-1][j]],
                            [matriz[i][j+1]],
                            [matriz[i][j-1]],
                            [matriz[i+1][j+1]],
                            [matriz[i-1][j-1]],
                            [matriz[i+1][j-1]],
                            [matriz[i-1][j+1]]
                            ]
                # quando morta
                if val == 0:
                    if vizinhas.count(1) == 3:
                        print(i, j)
                        print(vizinhas)
                        matriz[i][j] = 1

                # quando viva
                if val == 1:
                    pass

for i in matriz:
    print("".join(map(str, i)))